# How the web works?

## Intro
The web is made of two main parts, Front End and Back End

What we see and interact with is the Front End 

The Back End are all of the parts of the web the users don't interact with



## How does it everything works on the web?

##### The URL request
The server receives a request from the client in the form of a URL 
From this URL the server can get almost all of the information to process the request

*http://example.com/path?query=value*

**http** HTTP is the Protocol, it tells the server if the request is encrypted
HTTP is a Non-Encrypted request
HTTPS is a Encrypted request

**example.com** Host or Domain Name, it tells the internet which server to send the response to
Each server has their own particular host so once the request gets to the server, it will take the request from that host
*youtube.com* is the host for the youtube server, so the youtube server already knows that all requests it gets will have the host youtube.com

**path** The Path tells the server what the client wants and defines which section of code on the server should be run in order to get the correct response
*/users /cats or /dogs* are an example of paths

**?query=value** The Query string is used by the specific section of the server to alter the response
The query string is broken down into an specific query parameters that determine the way the server response to a request for an specific path
*http://www.youtube.com/results?search_query=dogs* this example tells the server that we want videos of dogs

The url alone is not enough to tell the server exactly what it needs to do exactly what it needs to do, it can tell the server what section to look for and how to alter that section based on the query parameters

But that part of the server is broken down even further into multiple different parts
To determine which part of that section the server should run, it needs to use an action which is passed along with the url
The actions can either be

- GET
- POST
- PUT
- DELETE

By combining the action and the path the server can find the correct part of the correct section that it needs to run
It can then use the query parameters to alter the response of that particular part and section
Normally the response from the server would be an HTML page that is dynamically generated based on the request from the client
That's why on youtube the search page is always the same, since it has the same path and action
But the videos returned from our search are different based on the query parameters from our search

Another important thing to know about the server is that is only accesible to the outside world trought the sections that it defines
Which means that it's possible store any secure information and it'll be safe as long as it's not exposed trought an specific path 
It's safe to have a website and a database running on the same server, since the server only chooses to expose the website and not the database
Esentially the server acts as a barrier between the outside world and all the parts of the website



## Back End Development

## Basic Skills
##### Frontend Development
- UX or User Experience
- HTML, CSS & JavaScript
- Frontend Frameworks
- UI or User Interface
- Git version control
- NPM, Webpack, Parcel, Babel, Sass
- HTTP, JSON, APIs
- Designing skills

##### Backend Development
- Foundation & Structure
- Server Side Language
- Server Side Framework
- Database, SQL, ORM
- Request / Response Cycle
- Security
- Visualization & Containers
- Production Env & Devops

##### Fullstack Development
- Frontend tech
- Backend tech
- Total independence to build any project combining front and back skills
