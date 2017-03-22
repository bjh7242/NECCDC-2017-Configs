<script>
$( document ).ready(function() {
  $( "#add_user" ).submit(function( event ) {
    event.preventDefault();
    var valid = "True";
    $.get( "check_username.php?uname=" + $("#username").val().trim(), function( data ) {
       if(data.trim()=="invalid"){
         $("#username").addClass( "bad" );
	 valid = "False";
       }else{
         $("#username").removeClass( "bad" );
       } 
   });
    
    var re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    if(!re.test($("#email").val())){
	$("#email").addClass( "bad" );
        valid = "False";
    }else{
	$("#email").removeClass( "bad" );
    }
    if($("#password").val() != $("#confpassword").val() | $("#password").val() == ""){
        $("#password").addClass( "bad" );
	$("#confpassword").addClass( "bad" );
        valid = "False";
	
    }else{
	$("#password").removeClass( "bad" );
        $("#confpassword").removeClass( "bad" );
    }
    if(valid == "True"){
      var dat = $(this).serializeArray();
      $.post( "add_user.php", dat, function( data ) {
      	$("#result").html(data);
	setTimeout(function() {
		window.location.href = 'index.php?page=signin.html'; 
	}, 2000);
      });
    }
  });
});

</script>

<div id="content" style="text-align:left;">
<div id="result"></div>
<form id="add_user">
<label for="username">Username:</label><input class="focus" name="username" id="username" type="text" placeholder="Enter Username" />
<label for="email">Email:</label><input class="focus" name="email" id="email" type="text" placeholder="Enter Email" />
<label for="password">Password:</label><input class="focus" name="password" id="password" type="password" placeholder="Enter Password"/>
<label for="confpassword">Confirm Password:</label><input class="focus" id="confpassword" type="password" placeholder="Enter Password Confirmation" />
<input id="sub" type="submit" />
</form>

</div>
