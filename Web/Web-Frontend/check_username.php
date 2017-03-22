<?php
if(!isset($_GET['uname'])){
	echo "invalid";
	exit();
}
$uname = $_GET['uname'];
include("common.php");
$sql = "SELECT * FROM users where username='".$uname."'";
if($result = $link->query($sql)){
    if($result->num_rows > 0 or $_GET['uname'] == "") {
        echo "invalid";
    }else{
	echo "valid";
    }
}
?>

