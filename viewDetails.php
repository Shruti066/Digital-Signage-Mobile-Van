<?php
	$dbHost     = 'localhost';
	$dbUsername = 'admin';
	$dbPassword = 'admin';
	$dbName     = 'advertise';

	$db = new mysqli($dbHost, $dbUsername, $dbPassword, $dbName);
	if($db->connect_error)
	{
		die("Connection failed: " . $db->connect_error);
	}
	else
	{
		$sql = "SELECT * FROM advertise.adv ORDER BY id DESC LIMIT 1";
		$result = $db->query($sql);

		while($row = $result->fetch_assoc())
		{
			echo  $row["info"]."@@".$row["link"]."@@".$row["image"];
		}
	}
	$db->close();
?>
