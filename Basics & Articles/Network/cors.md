# CORS / Cross-Origin Resource Sharing

**CORS** or **Cross-Origin Resource Sharing** is a mechanism that allows a website on one URL to request data from a different URL
Sometimes when we try to reach a resource on our website that is located in a different URL we cannot access it, or when we try to fetch data from our API and then fails with a CORSS error in the Console

This happens a lot because the browser implements the **Same-Origin Policy** as part of its security model, which allows a website to freely request images and data from its own URL but blocks anything from an external URL unless certains conditions are met
When the browser makes a request it adds an *Origin Header* to the request message, if that request goes to a server on the same origin, then its allowed without questions
However if that request goes to a different URL	that is known as a *cross-origin request*

When sending the response, the server will add the *Access-Control-Allow-Origin* header
Its value needs to match the Origin Header on the Request

## CORS Security
### Is it safe to access any url?
In modern browsers, each tab runs on an independent process or [sandboxed](https://wiki.mozilla.org/Security/Sandbox/Process_model), therefore js scripts cannot access or modify memory spaces outside of the process

It cannot acces neither *localStorage* nor *Cookies* associated to another domain, due to the [Same Origin](https://en.wikipedia.org/wiki/Same-origin_policy#Origin_determination_rules) policy.

The main problem would be to download & execute a binary file or inserting personal info.

#### Browsers exploits / Beef Project
From another point of view, on 2023 no one is targeting cookies, there is much bigger risk for browsers, for example [Beef Project](https://beefproject.com/)
Is it possible to create malicious urls with beefproject.com and take control of the PC/mobile


### Response Headers

```txt
HTTP/1.1 200 OK
X-Powered-By: Express
Access-Control-Allow-Origin: http://localhost:5000
Vary:Origin
Content-Type: application/json; charset=utf-8
Content-Length: 23
ETag: W/"17-5bdkTCO43EEL9K1bdRBu8k2HqAU"
Date: Mon, 29 Mar 2021 12:47:12 GMT
Connection: keep-alive
```

### Request Headers

```txt
GET /HTTP/1.1
Host: localhost: 3000
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64)
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Enconding: gzip, deflate
Referer: http://localhost:5000/
Origin: http://localhost:5000
```

If there's a mismatch, the browser will prevent the response data from being shared with the client
This results as an error in the browser, but for security reasons, there's limited information about what actually wen wrong

## Solution
The solution to a CORS error relies on the server, this means we have to control the server
If we have control on the server, we must configure it to respond with the proper header
```javascript
const express = require('express');
const app = express();
const cors = require('cors');

# In express.js this can be achieved with the following line, it tells the server to include the CORS headers on every response
app.use(cors({origin: https://foo.com}));
app.get('/', (req, res) => {
	res.status(200).json({title: 'hello world'})
});
```

Now certain HTTP request like PUT or any request with a non-standard header will need to be preflighted
which would be like a sanity check in the airport that ensures the passenger or request that is safe to fly on the internet

The browser automatically knows when to preflight and will first make a request using the option http verb
the server will then respond saying yes, I allow this origin to make request with the following methods
**OPTIONS** 
*Origin: foo.com*

**204**
*Access-Control-Allow-Origin: foo.com*
*Access-Control-Allow-Methods: PUT*

At which point, the main request can happen without a problem
The server can respond with a max age header allowing the browser to cache a preflight for a certain amoint of time

**Preflight Caching**
*Access-Control-Max-Age: 86400*
