var https = require('https');
var fs = require('fs');
 
var options = {
    hostname: 'localhost',
    port:8000,
    path:'/',
    method:'GET',
    key:fs.readFileSync('privatekey.pem'),
    cert:fs.readFileSync('certificate.pem'),
    ca:[fs.readFileSync('certrequest.csr')],
    rejectUnauthorized:false
};
 
options.agent = new https.Agent(options);
 
var req = https.request(options,function(res) {
    res.setEncoding('utf-8');
    res.on('data',function(d) {
        console.log(d);
    });
});
req.end();
 
req.on('error',function(e) {
    console.log(e);
});
