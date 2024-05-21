#!/usr/bin/node
# This script computes the number of tasks completed by user id

const request = require('request');
const url = process.argv[2];

request(url, function (err, response, body) {
	if (err) {
		console.log(err);
	} else if (response.statusCode === 200) {
		const completed = {};
		const task = JSON.parse(body);
		for (const i in tasks) {
			const task = task[i];
			if (task.completed === true) {
				if (completed[task.userId] === undefined) {
					completed[task.userId] = 1;
				} else {
					completed[task.userId]++;
				}
			}
		}
		console.log(completed);
	} else {
		console.log('An error occured');
	}
});
