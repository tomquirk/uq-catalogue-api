var promise = require('bluebird');

var options = {
  promiseLib: promise
};

var pgp = require('pg-promise')(options);
var connectionString = 'postgres://tomquirk:@localhost:5432/uq_catalogue';
var db = pgp(connectionString);

module.exports = {
  getAllCourses: function(req, res, next) {
    db.any('select * from course')
      .then(function(data) {
        res.status(200)
          .json({
            status: 'success',
            data: data
          });
      })
      .catch(function(err) {
        return next(err);
      });
  }
}