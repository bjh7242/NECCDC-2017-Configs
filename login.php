<?php 
include_once("common.php");
if(!isset($_POST['password']) or !isset($_POST['username'])){
	exit("Error: You must provide parameters");
}
$username = $_POST['username'];
$password = $_POST['password'];
$sql = "SELECT * FROM users WHERE username='$username' and password='$password'";
if($result = $link->query($sql)){
	if($result->num_rows >= 1){
		echo json_encode("Success: Login");
	}else{
		echo json_encode("Error: " . "Invalid Password");
	}
}else{
	echo json_encode("Error: " . $mysqli->error);
}
?>