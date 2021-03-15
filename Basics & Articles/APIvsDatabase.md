# Restful API vs Database

There are reasons to use a REST API, when we have an app that will be available to the public, we don't want to write our SQL queries directly in our code, as well as the credentials to connect to our server

Anyone with the knowledge could decompile our app and see our code and have access to the credentials to our database server
The good approach is to write an REST API to handle the flow of data between our app and database, since REST API should be designed to be accesed publicy, we'll only have to pass in the data, or just call the API we need
We don't need the server credentials to connect

If we're going local, then we could use the database approach of ours, since our app will be used only by our clients
