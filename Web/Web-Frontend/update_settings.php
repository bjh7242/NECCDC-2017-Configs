<?php
include_once("common.php");
include_once("session.php");
$user=$_POST['username'];
$pass=$_POST['password'];
$newpass=$_POST['new_password'];
$email=$_POST['email'];
if($newpass!=""){
	$sql = "Select * from users where username='$user' and password='$pass'";
	if($result = $link->query($sql)){
		if($result->num_rows > 0){
			$sql = "UPDATE `users` SET password='$newpass' where username='$user'";
			$link->query($sql);
			echo 'updated password';
		}else{
			echo "password not update";
		}
	}	
}
$uid = $session['uid'];
$sql = "UPDATE `users` SET username='$user' where uid='$uid'";
$link->query($sql);

$sql = "UPDATE `users` SET email='$email' where uid='$uid'";
$link->query($sql);

echo "
<body onload='history.go(-1);'>
";
?>
