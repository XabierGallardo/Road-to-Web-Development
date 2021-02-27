# HTTP, HTTPS, SSL & Internet Protocols

## Introduction
Every communication sent through HTTP connections can be read by any hacker that has a connection between our browser and the web server
This is specially important if we are dealing with sensitive data (credit card info, personal data)
With a HTTPS connection, every communication is encrypted, so even in the connection is "sniffed" or intercepted, it's not possible to access the data

HTTPS (Hypertext Transfer Protocol Secure) is the secure version of HTTP
Browsers like Firefox and Chrome show a lock icon on the direction bar to show visually that the communication with the server is encrypted, which means, it has an HTTPS protocol

HTTPS pages use either SSL or TLS as the secure protocols to encrypt communications
Both use a PKI, an asymetric system that uses two keys to encrypt communications, a public key and a private key
Every encryption with the public key can only be decrypted with the private key and viceversa

## How does HTTP protocol works?
HTTP (HyperText Transfer Protocol) is a network protocol, this is a set or rules to follow to publish websites
HTTP is the core foundation of Internet or www (World Wide Web)

HTTP protocol works through a system between requests and responses
A **client**, using a internet browser and a **server**, the computer that hosts websites

The client sents a request to the server (*http request*)
The server response to the  client (*http response*) with data, it may be from HTML, to an image or any file the client knows how to handle
When we are visiting a website using our browser, we're using an http session to obtain everything we see as the final result (HTML, images, JavaScript code, etc)

The URI, known as *URL* that shows the browser on the top bar starts with http, which means that it's using http protocol to show us the page we're visiting

## HTTPS safe sessions
When the URL starts with HTTPS instead of http, it means that the browser is using an secure schema to protect the data that is being transfered
This HTTPS schema is the one that must use every commercial transaction on the Internet
This schema is known as *TSL*

A secure session adds encryption to cypher the transmitted data, this way, if the data is intercepted, the content cannot be visible without the proper keys

On a secure session there are being used certificates to make sure that the communication is being done properly with the correct person, avoiding an intermediary that could intercept the communication

## Example of a HTTP communication
**The clients makes a request to show the main page**
```sh
GET /principal.html HTTP/1.1
Host: www.pagina.com 
```

**The server sends a response to the client**
```sh
HTTP/1.1 200 OK
Date: Tue, 24 Feb 2016 22:38:34 GMT
Content-Type: text/html; charset=UTF-8
Content-Length: 75
Connection: close
<html>
<head>
<title>Título</title>
</head>
<body>
Nada aquí.
</body>
</html> 
```
