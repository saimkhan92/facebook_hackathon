var express = require('express');
var PythonShell = require('python-shell');

var app = express();

app.get('/', function(req, res) {

var arguments = []

arguments.push(req.query.name);
arguments.push(req.query.age);

var options = {
  args: arguments
};




    PythonShell.run('test.py', options, function (err, results) { 
  	res.type('text/plain');
  	res.send(results);
	});


});


app.get('script1', function(req, res) {

	PythonShell.run('script1.py', {}, function (err, results) { 
	console.log(results[0]);
	console.log(typeof results[0]);
  	res.type('text/plain');
  	res.send(results);
	});


});

app.get('script2', function(req, res) {

	PythonShell.run('script2.py', {}, function (err, results) { 
	console.log(results[0]);
	console.log(typeof results[0]);
  	res.type('text/plain');
  	res.send(results);
	});


});

//you can use error handling to see if there are any errors


console.log('program over');

app.listen(process.env.PORT || 8085);

