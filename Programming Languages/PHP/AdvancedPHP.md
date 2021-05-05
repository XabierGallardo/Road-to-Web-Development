# PHP Form Hanlding
Superglobal variables are built-in variables that are always available in all scopes
The PHP superglobals GET and POST are uset tocollect form-data


### PHP POST
```sh
#$_POST is a superglobal variable which is used to connect form data after sumitting an HTML form with method="post"

#$_POST is also widely used to pass variables
<html>
<body>

<form method="post" action"<?php echo $_SERVER['PHP_SELF']; ?>"
Name: <input type="text" name="fname">
<input type="submit">
</form>

<?php
if($_SERVER["REQUEST_METHOD"] == "POST") {

	$name = $_POST['fname'];

	if(empty($name)) {

		echo "Name is empty";

	} else {

		echo $name;

	}
}
?>
</body>
</html>
```

# PHP Sessions
A session is a way to store data in variables to be used accross multiple pages
Unlike a cookie, the information is not stored on the users computer

### What is a PHP Session
The web server does't know who we are and what do we do, because the HTTP address doesn't maintain state
Session variables solve this problem by storing user info to be used across multiple pages (username, favourito color, etc)
By default, session variables last until the user closes the browser

Session variables hold info about one single user and are available to all pages in one application

### Starting a PHP Session
The session_start() function must be the very first thing in your document, before any HTML tags
```sh
<?php
session_start();
?>

<!DOCTYPE html>
<html>
<body>

<?php
$_SESSION["favcolor"] = "green";
$_SESSION["favanimal"] = "cat";

echo "Session variables are set";
?>

</body>
<html>
```
