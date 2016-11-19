var moment = require('moment');
module.exports = {
  debug: function(msg) {
    var time = moment().format('YYYY-MMM-Do: h:mm:ss a')
    console.error(time, msg);
  }
}