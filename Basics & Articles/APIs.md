# API / Application Programming Interfaces

# Begginer friendly explanation
According to Wikipedia:

*REST or Representational state transfer is a software architectural style that defines a set of constraints to be used for creating Web services. RESTful Web services allow the requesting systems to access and manipulate textual representations of Web resources by using a uniform and predefined set of stateless operations*

REST is basically a set of rules for communication between a client and server. There are a few constraints on the definition of REST:

1. **Client-Server Architecture**: The user interface of the website/app should be separated from the data request/storage, so each part can be scaled individually.

2. **Statelessness**: The communication should have no client context stored on server. This means each request to the server should be made with all  the required data and no assumptions should be made if the server has any data from previous requests.

3. **Layered system**: Client should not be able to tell if it's communicating directly with the server or some intermediary. These intermediary servers (be it proxy or load balancers) allow for scalability and security of the underlying server.

### REST Client
The browser can act as an uncontrolled REST client (the website handles the browser requests).
The browser, for a long time, used an in-built function called XMLHttpRequest for all REST request.
But this was succeeded by FetchAPI, a modern, promise based approach to request.
Others examples are code libraries like axios, superagent and got or some dedicated apps like Postman, or a command line took like cURL.

### REST Service
The server.
There are many popular libraries that make creation of these servers a breeze, like ExpressJS for NodeJS and Django for Python

### REST API
This defines the endpoint and methods allowed to access/submit data to the server.
We will talk about this in great detail below. Other alternatives to this are: GraphQL, JSON-Pure and oData

### How does it work?
In broad terms, you ask the server for a certain data or ask it to save some data, and the server responds to the requests.

In programming terms, there is an endpoint (a URL) that the server is waiting to get a request.
We connect to that endpoint and send in some data about us (REST is stateless, no data about the request is stored) and the server responds with the correct response.

### Anatomy of REST
1. **Endpoint**: It's the URL where the REST Server is listening

2. **Method**: Earlier, I wrote that you can either request data or modify it, but how will the server know what kind of operation the client wants to perform? REST implements multiple 'methods' for different types of request, the following are most popular
*GET*: Get resource from the server
*POST*: Create resource to the server
*PATCH or PUT*: Update existing resource on the server
*DELETE*: Delete existing resource from the server

3. **Headers**: The additional details provided for communication between client and server. Some of the common headers are:

*Request* host (the IP of client), accept-language (language understandable by the client), user-agent (data about client, operating system and vendor)

*Response* status (the status of request or HTTP code), content-type (type of resource sent by server), set-cookie (sets cookies by server)

4. **Data**: Contains info you want to send to the server.



# API Explanation 

An API or *Application Programming Interface* is a way for 2 computers to talk to each other
Using an API would be like using a website on our browser
But instead of clicking buttons and filling out forms, we write code to explicity request data from a server

For example, we could visit the NASA website to look at asteroids or we could use their Rest API to request the raw JSON data that is shown on the screen
There are 3 main types, Private, Public and External

- Private APIs are classified as an in-house application for employees to automate business processes and delivery
- Public/Partner APIs are openly promoted but available for known developers or business partners
- External APIs are available to any third-party developer and are mostly designed or built for end-users/customers

APIs make it easier to access to a variety of resources
**APIs are efficient**, they can significantly reduce the amount of work and will speed up the development process of an application
**APIs make things simpler**

## API Specifications
##### Service Object Access Protocol / SOAP
SOAP is a lightweight protocol for exchanging structured information in a decentralized, distributed environment
This contains rules guiding requests and responses sent from web applications using XML between systems through HTTP

##### GraphQL
GraphQL is a query language for APIs, it provides an absolute and simplified description of the data in APIs, which gives us the power to get the exact data we need
This makes easier to evolve APIs over time and also enables powerful developer tools

##### Representational State Transfer (REST)
*Representational State Transfer* or *REST* is a style of architecture that provides standars on the web between computer systems which makes communication flow easier within applications
REST APIs are stateless and can be used for seperation of concecrns between the client and the server

**RESTful** means they follow a set of rules or constraints known as **Representational State Transfer**, which has been the standard for API development since early 2000s


## How an API organizes the data?
A restful API organizes data entities or resources into a bunch of unique URLs or specifically URIs *Uniform Resource Identifiers*
URIs differentiate different types of data resources on a server *https://api.com/v2/comet*
```sh
https://api.com/v2
# Asteroid data
/asteroid
# Meteor data
/meteor
# Comet data
/comet

# Requesting asteroid data from an API
https://api.com/v2/asteroid
```

**https://api.com/v2** is the *Network Location*
**/comet** is the *Resource*

A client can get data about a resource by making a request to that endpoint over HTTP
The request message has a very specific format

## REQUEST
*The start line contains the URI we want to access* preceded by an HTTP verb or request which signal our intent with the resource
```sh
POST /dinosaur HTTP/1.1 
```
- **GET** / READ data
- **POST** / CREATE data
- **PATCH** / UPDATE data
- **DELETE** / DESTROY data

Below the start line we have the *Headers* that contain metadata about the request
```sh
Accept: application/json
Authorization: <token>
Connection: jeep-alive
```
- **Accept** header can tell the server we want the data in an specific format like *I only accept JSON*
- **Authorization** header can be used to tell the server that we're allowed to make that request

The body contains a custom payload of data
```sh
{
 "face": "anydata"
}
```
The server will receive the request message, then execute some code usualy to read from a database that can then be formatted into a response message

## RESPONSE
The top of the message contains a status code to tell the client what happened to their request
```sh
HTTP /1.1 200 OK
```
- **2xx** GOOD
- **4xx** Something WRONG with the request
- **5xx** Server BROKEN

After the status code we have the *Response Headers* which contain information about the server
```sh
Server: nginx
Age: 2323
Connection: keep-alive
```

Followed by the *Response Body* which contains the data payload and is usually formatted in JSON when talking about APIs
```sh
{
 "id": "123-xyz",
 "status": "success",
}
```

## About the architecture
The important part about this architecture is that it's **Stateless**
This means that the 2 parties don't need to store any info about each other, and every request response cycle is independent from all other communication
