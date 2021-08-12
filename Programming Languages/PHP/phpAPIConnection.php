<?php
//Display errors
ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);
?>

<!DOCTYPE html>
<html>

<head>

	<meta charset="utf-8">
	<title>PHP Crash Course</title>

	<style>
		body {font-family: FreeMono, monospace; font-size: large; color: white; background: #262626;}
	</style>

</head>

<body>

	
<?php

// Method: POST, PUT, GET etc
// Data: array("param" => "value") ==> index.php?param=value

function CallAPI($method, $url, $data = false) {

	#curl = curl_init();

	switch ($method) {
			
			case "POST":
				curl_setopt($curl, CURLOPT_POST, 1);

				if($data)
					curl_setopt($curl, CURLOPT_POSTFIELDS, $data);
				break;

			case "PUT":
				curl_setopt($curl, CURLOPT_PUT, 1);
				break;

			default:
				if($data)
					$url = sprintf("%s?%s", $url, http_build_query($data));

		}

		// Optional Authentication:
		curl_setopt($curl, CURLOPT_HTTPAUTH, CURLAUTH_BASIC);
		curl_setopt($curl, CURLOPT_USERPWD, "username:password");

		curl_setopt($curl, CURLOPT_URL, $url);
		curl_setopt($curl, CURLOPT_RETURNTRANSFER, 1);

		$result = curl_exec($curl);

		curl_close($curl);

		return $result;
}

?>

</body>

</html>
