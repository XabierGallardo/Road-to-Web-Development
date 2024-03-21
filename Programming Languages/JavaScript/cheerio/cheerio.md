# Cheerio

A library used for Web Scraping using Node.js

We can extract info or a full website using jQuery to select specific parts

## First steps

```sh
# Install nodejs, npm & cheerio
sudo apt update
sudo apt install nodejs npm
npm install cheerio

# Create a package .json
npm init -y

# Install cheerio and request (lightweight http module to make request)
npm i cheerio request
```

## Doing the basics on scrape.js
Code on scrape.js
```javascript
//Bring dependencies
const request = require('request');
const cheerio = require('cheerio');

//URL
request('putyoururl.com', (error, response, html) => {

	//Successful http response
	if(!error && response.statusCode == 200) {



		/*	jQuery methods to get data	*/

		//We'll use a $ variable to select from DOM like if we were using jQuery
		const $ = cheerio.load(html);
		
		//We'll get info from header
		const siteHeading = $('#logo');
		
		//Get plain html
		//console.log(siteHeading.html());

		//Get text inside the html tags
		//console.log(siteHeading.text());

		//Get text with find method
		//const output = siteHeading.find('h1').text();

		//Get text with children method
		//const output = siteHeading.children('h1').text();
		
		//Get text with next method
		//const output = siteHeading.children('h1').next().text();
		
		//Get text with parent method
		//const output = siteHeading.children('h1').parent().text();
		//console.log(output);



		/*	How to loop over elements	*/
		$('.content_reference span').each((i, el) => {
			
			//Iteration through all span elements of an specific class
			const item = $(el).text();
			console.log(item);

			//Get link inside the element
			const link = $(el).attr('href');
```


## Looping on scrape2.js
Code on scrape2.js
```javascript
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
```
