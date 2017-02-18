const express = require('express');
const router = express.Router();

const db = require('./queries');

router.get('/api/programs', db.getPrograms);
router.get('/api/program/:programCode', db.getProgram);

router.get('/api/plans/:programCode', db.getProgramPlans);
router.get('/api/plan/:planCode', db.getPlanCourses);

module.exports = router;