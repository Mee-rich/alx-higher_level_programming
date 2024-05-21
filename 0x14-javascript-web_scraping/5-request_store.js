#!/usr/bin/node
// This script gets the contents of a webpage and stores it in a file

const fs = require('fs');
const request = require('request');
const url = process.argv[2];


request(url, function (err, response, body) {
	if (err == null) {
		fs.writeFileSync(process.argv[3], body);
	}
});

