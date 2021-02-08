//Bring dependencies
const request = require('request');
const cheerio = require('cheerio');

//URL
request('https://lipsum.com/', (error, response, html) => {

	//Successful http response
	if(!error && response.statusCode == 200) {
		console.log(html);
	}
});
