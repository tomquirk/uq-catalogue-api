const express = require('express');
const path = require('path');
const cookieParser = require('cookie-parser');
const bodyParser = require('body-parser');

const routes = require('./routes');
// const logger = require('./logger');

const app = express();

// if (app.get('env') === 'production') {
//   app.use(logger);
// }

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));
app.use(cookieParser());

// CORS headers
app.use((req, res, next) => {
  res.header("Access-Control-Allow-Origin", "*");
  res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
  next();
});

app.use('/', routes);

// catch 404 and forward to error handler
app.use((req, res, next) => {
  const err = new Error('Not Found');
  err.status = 404;
  next(err);
});

/* dev error handler */
if (app.get('env') === 'development') {
  app.use(function(err, req, res, next) {
    res.status(err.code || 500)
      .json({
        status: 'error',
        message: err
      });
  });
}

/* prod error handler */
app.use((err, req, res, next) => {
  res.status(err.status || 500)
    .json({
      status: 'error',
      message: err.message
    });
});

module.exports = app;