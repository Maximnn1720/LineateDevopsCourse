var express = require('express');
var app = express();

function fibo(n) {
    if (n <= 2)
        return 1;
    else return fibo(n - 1) + fibo(n - 2);
}

app.get('/', function(req, res){
    console.log('/ endpoint was hit');

    let num = parseInt(30);
    res.send('Hello World my darling ' + fibo(num));
});

var server = app.listen(3000, function() {
    console.log('Example app listening on port 3000');
});

module.exports = server;