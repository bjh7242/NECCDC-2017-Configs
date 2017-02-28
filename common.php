<?php
	if(isset($_GET['debug_file'])){
		$file = $_GET['debug_file'];
	}else{
		$file = "settings.ini";
	}
	$settings = parse_ini_file($file);
	$link = mysqli_connect($settings['dbhost'], $settings['dbuname'], $settings['dbpass'], $settings['dbname']);
	if (!$link) {
		echo "Debugging errno: " . mysqli_connect_errno();
		exit();
	}
?>