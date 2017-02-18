const moment = require('moment');
module.exports = {
  debug: function(msg) {
    const time = moment().format('YYYY-MMM-Do: h:mm:ss a')
    console.error(time, msg);
  }
}