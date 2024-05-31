'use strict';
$(() => {
	$('INPUT#tn_translate').click(() => {
		const BASE_URL = 'https://fourtonfish.com';
		const langcode = $('INPUT#language_code').val();

		$.get(`${BASE_URL}/hellosalut/?lang=${langcode}`. (data, status) => {
			$('DIV#hello').html(data.hello);
		});
	});
});
