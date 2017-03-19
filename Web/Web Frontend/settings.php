<?php
include_once('common.php');
include_once('session.php');
$sql = "select * from users where uid=".$session['uid'];
if($result = $link->query($sql)){
    while ($row = $result->fetch_assoc()) {
	$pass = $row['password'];
	$user = $row['username'];
	$email = $row['email'];
    }
}

?>

<div id="content">
	<?php
	if(isset($session['logged_in']) and $session['logged_in'] == True){
	echo '
		Here you can update your profile settings. 
		<div id="update_box">
		<form action="update_settings.php" id="doit" method="post">
			<label>
				Username:
				<input id="username" name="username" type="text" value="'. $user.'"/>
			</label>
			<label>
				Current password:
				<input id="password" name="password" type="password" value="'. $pass.'" />
			</label>
			<label>
				New password:
				<input id="password" name="new_password" type="password" />
			</label>		
			<label>
				Email Address:
				<input id="email" name="email" type="text" value="'.$email.'"/>
			</label>
			<input type="submit" />
		</form>	
		</div>
	';
	}else{
		echo "You must log in to view this page.";
	}
	?>
</div>
