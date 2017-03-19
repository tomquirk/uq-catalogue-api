const promise = require('bluebird');

const options = {
  promiseLib: promise
};

const pgp = require('pg-promise')(options);
const connectionString = 'postgres://tomquirk:@localhost:5432/uq_catalogue';
const db = pgp(connectionString);

module.exports = {
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
    db.any('SELECT program.*,\
            (\
                select array_to_json(array_agg(row_to_json(t)))\
                from (\
                  SELECT plan_code, title\
                    FROM plan\
                    WHERE program_code = ${programCode}\
                ) t\
            ) as plan_list\
            FROM program\
            WHERE program_code = ${programCode}', req.params)

      .then(data => {
        res.status(200)
          .json({
            status: 'success',
            data: data[0]
          });
      })
      .catch(err => next(err));
  },
  getPlan(req, res, next) {
    db.any('SELECT plan.*,\
            (\
              select array_to_json(array_agg(row_to_json(t)))\
              from (\
                SELECT course.course_code, course.title, course.description,\
                  course.raw_prerequisites, course.units, course.course_profile_id,\
                  (\
                    select row_to_json(t)\
                    from (\
                      SELECT semester_1 as "1", semester_2 as "2", summer_semester as "summer"\
                      FROM course c\
                      WHERE c.course_code = course.course_code AND course.invalid = false\
                  ) t\
                  ) as semester_offerings\
                FROM course\
                LEFT JOIN plan_course_list\
                  ON course.course_code = plan_course_list.course_code\
                WHERE plan_course_list.plan_code = ${planCode} AND course.invalid = false\
            ) t\
            ) as course_list\
            FROM plan\
            WHERE plan_code = ${planCode}', req.params)

      .then(data => {
        res.status(200)
          .json({
            status: 'success',
            data: data[0]
          });
      })
      .catch(err => next(err));
  },
  getCourse(req, res, next) {
    db.any('SELECT course.course_code, course.title, course.description,\
            course.raw_prerequisites, course.units, course.course_profile_id,\
            (\
                select array_to_json(array_agg(t))\
                from (\
                  SELECT incompatible_course_code as course_code\
                  FROM incompatible_courses\
                  WHERE course_code = ${courseCode}\
                ) t\
            ) as incompatible_courses,\
            (\
                select row_to_json(t)\
                from (\
                  SELECT semester_1 as "1", semester_2 as "2", summer_semester as "summer"\
                  FROM course\
                  WHERE course_code = ${courseCode}\
                ) t\
            ) as semester_offerings\ FROM course WHERE course_code = ${courseCode}', req.params)
      .then(data => {
        res.status(200)
          .json({
            status: 'success',
            data: data[0]
          });
      })
      .catch(err => next(err));
  }
}