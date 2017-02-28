<?php
include_once("common.php");
if(isset($_COOKIE["PHPSESSID"])){
	$session = array();
	$sess_id = $_COOKIE["PHPSESSID"];
	$sql = "SELECT sessions.uid,users.uid,users.username FROM sessions INNER JOIN users ON sessions.uid = users.uid where session='$sess_id' ";
	if($result = $link->query($sql)){
		if($result->num_rows >= 1){
			$row = $result->fetch_array(MYSQLI_ASSOC);
			print_r($row);
			$session['logged_in'] = True;
			$session['username'] = $row['username'];
			$session['uid'] = $row['uid'];
		}else{
			$session = array();
		}
	}else{
		echo "Error: " . $link->error;
		$session = array();
	}
}else{
	$session = array();
}

?>