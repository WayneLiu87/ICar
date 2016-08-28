/**
 * Created by aaronyang on 2015/10/30.
 */
var https=require('https');
var fs=require('fs');
var privatekey=fs.readFileSync('privatekey.pem');
var pc=fs.readFileSync('certificate.pem');
var options={
  key:privatekey,
  cert:pc
}
var server=https.createServer(options, function (req,res) {
  console.log(req.url);
  if(req.url!=='favicon.ico'){
    res.setHeader('Content-Type','text/html');
    res.write('<html><head><meta charset="utf-8"/> </head>');
    res.write('hello ay！https服务');
    res.end();
  }
})
server.listen(1443,'0.0.0.0', function () {
  console.log('服务器开始监听');
})
