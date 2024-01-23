var express = require('express');
var app = express();

app.get('/', function(req, res){
    console.log('/ endpoint was hit');
    res.send('Hello World my darling');
});

var server = app.listen(3000, function() {
    console.log('Example app listening on port 3000');
});

module.exports = server;