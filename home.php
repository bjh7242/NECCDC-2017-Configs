<html>
	<head>
		<title>Fan.Tasy</title>
		<link rel="stylesheet" type="text/css" href="style.css">
	</head>
	<body>
		<?php 
		if(!isset($_GET['page'])){
			$site = "home.html";
		}else{
			$site = $_GET['page'];
		}
		?>
		<?php include("header.html"); ?>
		<?php include($site); ?>
		<?php include("footer.html"); ?>
	</body>
</html>