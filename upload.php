<?php
     
	$dbHost     = 'localhost';
	$dbUsername = 'admin';
	$dbPassword = 'admin';
	$dbName     = 'advertise';

	$info =  $_POST['info'];
	$link =  $_POST['link'];
	$image =  $_POST['image'];

	$db = new mysqli($dbHost, $dbUsername, $dbPassword, $dbName);
	if($db->connect_error)
	{
		die("Connection failed: " . $db->connect_error);
	}
	else
	{
		$insert = $db->query("INSERT into advertise.adv (info,link,image) VALUES ('$info','$link','$image')");
		if($insert)
		{
			echo "File uploaded successfully.";
		}
		else
		{
			echo "File upload failed, please try again.";
		} 
			
    	}
	$db->close();
?>