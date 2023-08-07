const express = require('express');
// Initialize app
const app = express();
const port = 3500;

// GET callback function returns a response message
app.get('/', (req, res) => {
	res.send('Hello World! Welcome to Node.js');
});

app.listen(port, () => {
	console.log(`Server listening at http://localhost:${port}`);
});