# API / Application Programming Interfaces

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