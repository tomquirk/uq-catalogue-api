const express = require('express');
const router = express.Router();

const db = require('./queries');

router.get('/api/programs', db.getPrograms);
router.get('/api/program/:programCode', db.getProgram);

router.get('/api/plan/:planCode', db.getPlan);

router.get('/api/course/:courseCode', db.getCourse);

module.exports = router;