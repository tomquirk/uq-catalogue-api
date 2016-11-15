var mysql = require('mysql');
var _ = require('lodash');
var Q = require('q');
// var nodemailer = require('nodemailer');

function REST_ROUTER(router, connection, md5) {
  var self = this;
  self.handleRoutes(router, connection, md5);
}

REST_ROUTER.prototype.handleRoutes = function (router, connection, md5) {

  router.get('/', function (req, res) {
    res.status(204).send('');
  });

  router.get('/contact', function (req, res) {
    console.log(req)

    // // create reusable transporter object using the default SMTP transport
    // var transporter = nodemailer.createTransport('smtps://user%40gmail.com:pass@smtp.gmail.com');

    // // setup e-mail data with unicode symbols
    // var mailOptions = {
    //   from: '"Fred Foo 👥" <foo@blurdybloop.com>', // sender address
    //   to: 'bar@blurdybloop.com, baz@blurdybloop.com', // list of receivers
    //   subject: 'Hello ✔', // Subject line
    //   text: 'Hello world 🐴', // plaintext body
    //   html: '<b>Hello world 🐴</b>' // html body
    // };

    // // send mail with defined transport object
    // transporter.sendMail(mailOptions, function (error, info) {
    //   if (error) {
    //     return console.log(error);
    //   }
    //   console.log('Message sent: ' + info.response);
    // });
  });

  router.get('/program/:program_code', function (req, res) {
    if (/[0-9]/.test(req.params.program_code) && req.params.program_code.length != 4) {
      res.status(404).json({ "message": "Invalid program" });
    }

    function program() {
      var defered = Q.defer();
      var query = 'SELECT * FROM Program where program_code = ?';
      var table = [req.params.program_code];
      query = mysql.format(query, table);
      connection.query(query, defered.makeNodeResolver());
      return defered.promise;
    }

    function program_plan_list() {
      var defered = Q.defer();
      var query = 'SELECT * FROM Plan WHERE program_code = ?';
      var table = [req.params.program_code];
      query = mysql.format(query, table);
      connection.query(query, defered.makeNodeResolver());
      return defered.promise;
    }

    Q.all([program(), program_plan_list()]).then(function (results) {
      if (results[0][0].length === 0) {
        res.status(404).json({ "message": "Program not found" });
      }
      var data = results[0][0][0];
      data.plan_list = results[1][0];
      res.status(200).json(data);
    });
  });

  /*
  Returns data for a single course
  */
  router.get('/course/:course_code', function (req, res) {
    if (/^\w+$/.test(req.params.program_code) && req.params.program_code.length != 8) {
      res.status(404).json({ "message": "Invalid course" });
    }
    function course() {
      var defered = Q.defer();
      var query = 'SELECT * FROM Course WHERE course_code = ?';
      var table = [req.params.course_code];
      query = mysql.format(query, table);
      connection.query(query, defered.makeNodeResolver());
      return defered.promise;
    }

    function semesters() {
      var defered = Q.defer();
      var query = 'SELECT semester_offering FROM Course_Semester_Offering WHERE course_code = ?';
      var table = [req.params.course_code];
      query = mysql.format(query, table);
      connection.query(query, defered.makeNodeResolver());
      return defered.promise;
    }

    Q.all([course(), semesters()]).then(function (results) {
      if (req.params.course_code === 'MEME9000') {
        res.status(418).json({ "message": "Blaze it" });
      } else if (results[0][0].length === 0) {
        res.status(404).json({ "message": "Course not found." });
      }
      var data = results[0][0][0];
      //get semester offerings
      data.semester_offerings = []
      _.each(results[1][0], function (sem) {
        data.semester_offerings.push(sem.semester_offering)
      })
      res.json(data);
    });
  });

  /*
  Returns data for a plan (major)
  */
  router.get('/plan/:plan_code', function (req, res) {
    if (/^\w+$/.test(req.params.program_code) && req.params.program_code.length != 10) {
      res.status(404).json({ "message": "Invalid plan" });
    }
    function plan() {
      var defered = Q.defer();
      var query = 'SELECT * FROM Plan where plan_code = ?';
      var table = [req.params.plan_code];
      query = mysql.format(query, table);
      connection.query(query, defered.makeNodeResolver());
      return defered.promise;
    }

    function plan_course_list() {
      var defered = Q.defer();
      var query = 'SELECT * FROM Course WHERE course_code in (SELECT course_code from Plan_Course_list WHERE plan_code = ?)';
      var table = [req.params.plan_code];
      query = mysql.format(query, table);
      connection.query(query, defered.makeNodeResolver());
      return defered.promise;
    }

    function course_semester_offerings() {
      var defered = Q.defer();
      var query = 'SELECT * FROM Course_Semester_Offering WHERE course_code in (SELECT course_code FROM Plan_Course_list WHERE plan_code = ?)';
      var table = [req.params.plan_code];
      query = mysql.format(query, table);
      connection.query(query, defered.makeNodeResolver());
      return defered.promise;
    }

    Q.all([plan(), plan_course_list(), course_semester_offerings()]).then(function (results) {
      if (results[0][0].length === 0) {
        res.status(404).json({ "message": "Plan not found." });
      }
      var data = results[0][0][0];
      data.course_list = results[1][0];

      //get semester offerings
      _.each(data.course_list, function (course) {
        course.semester_offerings = []
        _.each(results[2][0], function (sem) {
          if (sem.course_code === course.course_code) {
            course.semester_offerings.push(sem.semester_offering)
          }
        })
      })

      //get prerequisite sets

      res.json(data);
    });
  });

}

module.exports = REST_ROUTER;
