#!/usr/bin/node
# This script displays the status code of a GET request

const request = require('request');
const url = process.argv[2];

reques(url, function (err, response) {
	if (err) {
		console.log(err);
	} else {
		console.log('code: ' + response.statusCode);
	}
});
