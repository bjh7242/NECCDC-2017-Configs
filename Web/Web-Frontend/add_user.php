<?php
if(!isset($_POST['username']) or !isset($_POST['email']) or !isset($_POST['password'])){
	exit("You do not have the proper amount of inputs");
}
$uname = $_POST['username'];
$email = $_POST['email'];
$pass = $_POST['password'];
include("common.php");
$sql = "INSERT INTO `users` (`username`, `password`, `email`) VALUES ('".$uname."', '".$pass."', '".$email."');";
if($link->query($sql) === TRUE){
    echo "<font color=\"green\">Account created succesfully</font>";
    $id = mysqli_insert_id ( $link );
    $sql = "INSERT INTO `scores` (`uid`, `score`) VALUES ($id, 0)";
    $link->query($sql);

}else{
    echo "<font color=\"red\">Error: " . $sql . "<br>" . $link->error . "</font>";
}
?>
