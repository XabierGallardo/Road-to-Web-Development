# Ways of storing data in Node.js

#### Storing data in a global variable
Serving static pages for users can be suitable for landing pages or personal blogs
But of we want to deliver dynamic content, we must store the data somewhere

For example, an user signup case, we can server customized content for individual users or make it available for then after indentification only
If an user wants to sign up for our application, we may want to create a router handler to make it possible
```javascript
const users = [];

app.post('/users', function (req, res) {
	//retrieve user posted data from the body
	const user = req.body;
	users.push({
		name: user.name,
		age: user.age
	});
	res.send('successfully registered');
});
```
This way we can store the users in a global variable which will reside in memory for the lifetime of our app
Using this method has lots of cons
- RAM is expensive
- Memory resets each time we restart our app
- If we don't clean up, we'll end eventually with stack overflow


#### Storing data in a file
The next thing that comes up on our min is to store the data in files
If we store our user database permanently on the file system, we can avoid the previously listed problems
```javascript
const fs = require('fs');

app.post('/users', function (req, res) {
	const user = req.body
	fs.appendFile('users.txt', JSON.stringify({ nameL user.name, age: user.age}), (err) => {
		res.send('successfully registered');
	});
});
```
This way, we won't lose user data, not even after a server reset
This solution is also cost efficient, since buying storage is cheaper than buying RAM

Unfortunately, storing user data this way still has cons
- Appending is ok, but updating or deleting is not possible
- If we were working with files, there is no easy way to access them in parallel
- When we try to scale our application up, we cannot split files in between servers (It's possible though, but difficult!)


#### Storing data in SQL databases
SQL is a query language designed to work with relational databases
SQL databases have a couple of flavors depending on the product we're using, but the fundamentals are the same in each of them

The data itself will be stored in tables, and each inserted piece will be represented as a row in the table, like Google Sheets or Microsoft Excel

With an SQL database, we can define schemas, these schemas will provide a skeleton for the data we'll put in there
The types of the different values have to be set vefore we can store our data
For example, we must define a table for our user data, and have to tell the database that it has a username which is a string, and age, which is an integer

Among its advantages
- SQL enables communication with the databases and receibe answers to complex questions in seconds
- SQL views the data without storing the it in the object, it adheres to a long-established, clear standard
