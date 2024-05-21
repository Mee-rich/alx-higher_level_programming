#!/usr/bin/node
// This script prints all characters of a Star Wars movie.

const request = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/';

req.get(url + id, function (err, res, body) {
	if (err) {
		console.log(err);
	}
	const data = JSON.parse(body);
	const dt = data.characters;
	for (const i of dt) {
		req.get(i, function(err, res, body1) {
			if (err) {
				console.log(err);
			}
			const data1 = JSON.parse(body1);
			console.log(data1.name);
		});
	}
);
