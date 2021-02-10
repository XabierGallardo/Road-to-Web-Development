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
			console.log(link);
		});

	}
});
