#!/usr/bin/node
// This script prints all chracters of a Star Wars movie

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/films' + process.argv[2];

request(url, function (err, response, body) {
	if (!err) {
		const characters = JSON.parse(body).characters;
		printCharacters(characters, 0);
	}
});

function printCharacters (characters, index) {
	request(characters[index], function (err, response, body) {
		if (!err) {
			console.log(JSON.parse(body).name);
			if (index + 1 < characters.length) {
				printCharacters(characters, index + 1);
			}
		}
	});
}
