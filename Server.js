var express = require('express');
var mysql = require('mysql');
var http = require('http');
var reload = require('reload');
var bodyParser = require('body-parser');
var md5 = require('md5');
var rest = require('./REST.js');
var app = express();
var path = require('path');

process.env.NODE_ENV = 'dev';

function REST() {
  var self = this;
  self.connectMysql();
};

REST.prototype.connectMysql = function () {
  var self = this;
  var pool = mysql.createPool({
    connectionLimit: 100,
    host: 'localhost',
    user: 'root',
    password: '',
    database: 'uq_catalogue',
    debug: false
  });
  pool.getConnection(function (err, connection) {
    if (err) {
      self.stop(err);
    } else {
      self.configureExpress(connection);
    }
  });
}

REST.prototype.configureExpress = function (connection) {
  var self = this;
  app.set('port', process.env.PORT || 3000)
  app.use(bodyParser.urlencoded({
    extended: true
  }));

  app.use(express.static(path.join(__dirname, 'dist')));

  app.use(function (req, res, next) {
    res.header("Access-Control-Allow-Origin", "*");
    res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
    next();
  });

  app.use(bodyParser.json());
  var router = express.Router();
  app.use('/api', router);
  var rest_router = new rest(router, connection, md5);

  self.startServer();

}

REST.prototype.startServer = function () {
  var server = http.createServer(app)
  reload(server, app)
  app.listen(app.get('port'), function () {
    console.log("Listening on port " + app.get('port'));
  });
}

REST.prototype.stop = function (err) {
  console.log("ISSUE WITH MYSQL n" + err);
  process.exit(1);
}

new REST();
