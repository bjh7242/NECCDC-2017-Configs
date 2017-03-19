<?php
include("common.php");
$sql = "SELECT DISTINCT year FROM games";
$years = array();
if($result = $link2->query($sql)){
    while ($row = $result->fetch_assoc()) {
        array_push($years,$row['year']);
    }
}
?>

<script>
$( document ).ready(function() {
	$.get( "get_standings.php?year=<?php echo $years[0]; ?>", function( data ) {
	  $("#standings").html( data );
	});
$( "#year" ).change(function() {
        $.get( "get_standings.php?year="+$(this).val(), function( data ) {
          $("#standings").html( data );
        });
});
});
</script>
<div id="content">
<h1>Team Standings</h1>
Year Selection: 
<select id="year">
<?php
  foreach($years as &$value){
      echo '<option value="'.$value.'">'.$value.'</option>';
  }
?>
</select>
<center><div id="standings">Loading Standings...</div></center>
<br />
</div>
