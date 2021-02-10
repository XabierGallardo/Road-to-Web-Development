//Bring dependencies
const request = require('request');
const cheerio = require('cheerio');

//To write data to a file, fs module (file system module)
const fs = require('fs');
//CSV is a Comma Separated Values file, plain text files that contain structured data
const writeStream = fs.createWriteStream('post.csv');

//Write Headers
writeStream.write(`Title,Co,Ve \n`);

//URL
request('putyoururl.com', (error, response, html) => {

	if(!error && response.statusCode == 200) {

		const $ = cheerio.load(html);

		$('#tablepress-1').each((i, el) => {

			const title = $('.column-1').text();
			const co = $('.column-2').text();
			const ve = $('.column-3').text();

			//console.log('Title: ' + title + ' Co: ' + co + ' Ve: ' + ve);
			
			//Write Row to CSV
			writeStream.write(`${title},${co},${ve} \n`);

		});

		console.log('Scraping done...');

	}
});
