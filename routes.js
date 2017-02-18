var express = require('express');
var router = express.Router();

var db = require('./queries');

router.get('/api/programs', db.getPrograms);
router.get('/api/program/:programCode', db.getProgram);

router.get('/api/plans/:programCode', db.getProgramPlans);
router.get('/api/plan/:planCode', db.getPlanCourses);

module.exports = router;