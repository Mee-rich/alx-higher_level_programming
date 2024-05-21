#!/usr/bin/node
# This script prints the title of a Star Wars movie where the episode dnumber matches a a given integer

const request = require('request');
const EpisodeNum = process.argv[2];
const API_URL = 'https://swapi-api.alx-tools.com/api/films'

request(API_URL + EpisodeNum, function(err, response, body) {
	if (err){
		console.log(err);
	} else if (response.statusCode === 200) {
		const responseJSON = JSON.parse(body);
		console.log(responseJSON.title);
	} else {
		console.log('Error code: ' + response.statusCode);
	}
});
