const http = require('http');

http.createServer(function (req, res) {
    res.write('Hello World!');
    res.end();
}).listen(3000);
console.log("Server listen on http://127.0.0.1:3000");
