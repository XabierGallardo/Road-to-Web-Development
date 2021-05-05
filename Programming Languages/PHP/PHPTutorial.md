# PHP Tutorial

# INTRO
PHP: Hypertext Preprocessor is an open- source scripting language
PHP scripts are executed on the server, the result is returned to the browser as plain HTML

PHP can: 
- contain text, HTML, CSS, JavaScript and PHP code
- generate dynamic page content
- create, open, read, write, delete and close files on the server
- send and receive cookies
- add, delete, modify data on our database
- used to control user-access
- encrypt data
- output not only HTML, but images, pdf files and flash movies, text including XHTML and XML

About PHP:
- Runs on various platforms
- Compatible with almost all servers
- Supports a wide range of Databases
- Free, easy and runs efficiently on the server side


# Installation
Find a web host with PHP and MySQL support
Install a web server on your pc and then install PHP and MySQL

Creating some .php files and placing them onto our directory will make our server automatically parse them


# PHP Syntax
A PHP script can be placed anywhere in the document
A PHP script starts with **<?php** and ends with **?>**

The default file extension for PHP files is **.php**
A PHP file normally contains HTML tags and some PHP scripting code

PHP statements end with a semicolon **;**


# Comments
```sh
# // Single line comment

# # Also single line comment

# /* Multi line comment */
```


# Variables
In PHP a variable starts with the **$** sign
```sh
<?php
$text = "Hello World";
$x = 5;
$y = 10.5;
>?
```
- A variable starts with the **$** sign, followed by the name of the variable
- A variable must start with a letter or the underscore character
- A variable name cannot start with a number
- A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9 and underscore)
- Variable nnames are case-sensitive($age and $AGE are 2 different variables)

### Variables scope
In PHP, variables can be declared anywhere in the script
The scope of a variable is the part of the script where the variable can be referenced/used

PHP has three different variable scopes
- local
- global
- static

