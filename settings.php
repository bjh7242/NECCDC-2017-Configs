<?php
include_once('common.php');
include_once('session');
?>
<div id="content">
	<?php
	if(isset($session['logged_in']) and $session['logged_in'] == True){
	echo '
		Here you can update your profile settings. 
		<div id="update_box">
		<form action="doit" id="doit" method="post">
			<label>
				Username:
				<input id="username" name="username" type="text" />
			</label>
			<label>
				Current password:
				<input id="password" name="password" type="password" />
			</label>
			<label>
				New password:
				<input id="password" name="password" type="password" />
			</label>		
			<label>
				Email Address:
				<input id="email" name="email" type="text" />
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