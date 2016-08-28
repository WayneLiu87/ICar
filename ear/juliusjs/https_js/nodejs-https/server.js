var https = require('https')
	,fs = require("fs");
console.log('https');
var options = {
	key: fs.readFileSync('./privatekey.pem'),
	cert: fs.readFileSync('./certificate.pem')
};
console.log('options');
//console.log(fs.readFileSync('./privatekey.pem').toString());
//console.log(fs.readFileSync('./certificate.pem').toString());


var express = require('express'),
    app     = express();
app.use(express.static('../../dist'));
app.use(express.static(__dirname));


https.createServer(options, app).listen(8000, function(){
	console.log('Https server listening on port ' + 8000);
});

console.log('start');
