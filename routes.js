var express = require('express');
var router = express.Router();

var db = require('./queries');

router.get('/api/courses', db.getAllCourses);

module.exports = router;