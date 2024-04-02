# .gitignore Basics
When working with a private API key in a public repository, it's crucial to ensure that the key remains confidential and is not exposed to unauthorized users. One common practice is to use a `.gitignore` file to exclude sensitive files, such as configuration files containing API keys, from being tracked by Git and pushed to the public repository.

Here's how you can work with a private API key and `.gitignore` to keep it secure:

1. **Create a `.gitignore` file**: If you haven't already, create a `.gitignore` file in the root directory of your project.

2. **Add sensitive files to `.gitignore`**: Within the `.gitignore` file, specify the names or patterns of files that contain your private API key. For example:
   ```
   # Ignore files containing API keys
   api-keys.json
   credentials.json
   ```

3. **Store API keys in a separate configuration file**: Instead of hardcoding API keys directly into your code, store them in a separate configuration file (e.g., `config.json`, `secrets.json`, etc.). This file should not be tracked by Git and should be excluded using `.gitignore`.

4. **Use environment variables**: Another approach is to store API keys as environment variables on your development machine or server. In your code, access the API keys using environment variables rather than hardcoding them. This way, you can keep the actual API keys out of your codebase entirely.

5. **Secure your API keys on the server**: If you're deploying your application to a server, ensure that your API keys are securely stored and accessed. Avoid committing API keys to version control repositories on the server and instead use secure environment variables or configuration management tools to manage them.

6. **Encrypt sensitive files**: For an extra layer of security, you can encrypt sensitive files containing API keys before committing them to version control. This ensures that even if the files are accidentally exposed, the API keys remain protected.

By following these best practices and using `.gitignore` to exclude sensitive files, you can ensure that your private API keys remain secure while working with a public repository. It's essential to prioritize the security of your API keys to prevent unauthorized access and potential security breaches.


# Getting our .gitignore data onto our js app
Directly accessing sensitive information like API keys in client-side JavaScript can pose security risks, as it exposes your key to anyone who views the source code of your webpage. A more secure approach is to create a server-side application that handles requests to your API and keep your API key hidden on the server. However, if you must use client-side JavaScript for some reason, you can still do so, but exercise caution.

One way to use your API key in client-side JavaScript using `fetch` is by creating a server-side endpoint that serves your API key securely. Your client-side JavaScript code can then make a request to this endpoint to retrieve the API key.

Here's a basic example:

1. **Server-side Script (e.g., Node.js)**: Create a server-side script that serves the API key securely.

```javascript
// server.js
const express = require('express');
const fs = require('fs');
const app = express();

app.get('/api-key', (req, res) => {
  // Read the api-key.json file
  const apiKeyJson = fs.readFileSync('api-key.json');
  const apiKeyData = JSON.parse(apiKeyJson);
  res.json({ api_key: apiKeyData.api_key });
});

app.listen(3000, () => {
  console.log('Server is running on port 3000');
});
```

2. **Client-side JavaScript (index.html)**: In your HTML file, use `fetch` to request the API key from the server.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Using API Key</title>
</head>
<body>
  <script>
    // Make a fetch request to fetch the API key from the server
    fetch('http://localhost:3000/api-key')
      .then(response => response.json())
      .then(data => {
        // Now you have the API key, you can use it as needed
        console.log('API Key:', data.api_key);
      })
      .catch(error => console.error('Error fetching API key:', error));
  </script>
</body>
</html>
```

3. **Running the Application**: Start your Node.js server (`node server.js`), then open your `index.html` file in a browser. The JavaScript in `index.html` will make a request to the server endpoint (`/api-key`) using `fetch`, which will respond with the API key from the `api-key.json` file.

Remember to keep your API key secure and avoid exposing it in client-side code whenever possible.
