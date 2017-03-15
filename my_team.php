<?php
include("common.php");
include("session.php");
$sql = "Select * from teams where uid='".$session['uid']."'";
$playerIDs = array();
if($result = $link->query($sql)){
    $row = $result->fetch_assoc();
for( $i = 1; $i <= 25; $i++ ){ 
    $player = "player".$i;
    array_push($playerIDs,$row[$player]);
}
}
$playerNames = array();
foreach ($playerIDs as &$value) {
	$sql = "Select nameFirst, nameLast from master where playerID='". $value . "'";
	if($result = $link3->query($sql)){
		$row = $result->fetch_assoc();
		array_push($playerNames, $row['nameFirst'] . ' ' . $row['nameLast']);
	}
}
?>
<link rel="stylesheet" type="text/css" href="css/jquery.dataTables.css">
<script src="js/jquery-datatables.js"></script>
<script src="js/jquery.dataTables.js"></script>

<script>
$(document).ready(function() {
    $('#example').DataTable({"pageLength": 25});
} );
</script>
<div id="content">

<table id="example" class="display" cellspacing="0" width="100%">
        <thead>
            <tr>
		<th>Player No.</th>
                <th>Player Name</th>
                <th>Position</th>
                <th>Office</th>
                <th>Age</th>
                <th>Start date</th>
            </tr>
        </thead>
        <tfoot>
            <tr>
		<th>Player No.</th>
                <th>Player Name</th>
                <th>Position</th>
                <th>Office</th>
                <th>Age</th>
                <th>Start date</th>
            </tr>
        </tfoot>
        <tbody>
	    <?php
		$counter = 1;
		foreach ($playerNames as &$value) {
		echo '<tr>';
			echo '<td>'.$counter.'</td>';
			echo '<td>'.$value . '</td>';
			echo '<td>test</td>';
			echo '<td>test</td>';
                        echo '<td>test</td>';
                        echo '<td>test</td>';

		echo '</tr>';
		$counter++;
		}
	    ?>
	</tbody>
</table>

</div>
