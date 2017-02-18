const promise = require('bluebird');

const options = {
  promiseLib: promise
};

const pgp = require('pg-promise')(options);
const connectionString = 'postgres://tomquirk:@localhost:5432/uq_catalogue';
const db = pgp(connectionString);

module.exports = {
  getPlanCourses(req, res, next) {
    db.any('SELECT course.course_code, course.description, course.raw_prerequisites, \
      course.units, course.course_profile_id, plan_course_list.required FROM course \
    LEFT OUTER JOIN plan_course_list \
      ON course.course_code = plan_course_list.course_code \
    WHERE plan_course_list.plan_code = ${planCode}', req.params)
      .then(data => {
        res.status(200)
          .json({
            status: 'success',
            data
          });
      })
      .catch(err => next(err));
  },
  getPrograms(req, res, next) {
    db.any('SELECT * FROM program', req.params)
      .then(data => {
        res.status(200)
          .json({
            status: 'success',
            data
          });
      })
      .catch(err => next(err));
  },
  getProgram(req, res, next) {
    db.any('SELECT * FROM program WHERE program_code = ${programCode}', req.params)
      .then(data => {
        res.status(200)
          .json({
            status: 'success',
            data
          });
      })
      .catch(err => next(err));
  },
  getProgramPlans(req, res, next) {
    db.any('SELECT * FROM plan WHERE program_code = ${programCode}', req.params)
      .then(data => {
        res.status(200)
          .json({
            status: 'success',
            data
          });
      })
      .catch(err => next(err));
  }
}