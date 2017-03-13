<?php
if(!isset($_GET['year'])){
	exit("You do not have the proper amount of inputs");
}
$year = $_GET['year'];
include("common.php");
$sql = "SELECT * FROM games where year=$year";
$wins = array();
$losses = array();
if($result = $link2->query($sql)){
    /* fetch associative array */
    while ($row = $result->fetch_assoc()) {
	$h_sc = $row['hscore'];
	$a_sc = $row['ascore'];
	if($h_sc > $a_sc){
		if (array_key_exists($row['home'], $wins)){
			$wins[$row['home']] += 1;
		}else{
			$wins[$row['home']] = 1;
		}
                if (!array_key_exists($row['away'], $wins)){
                        $wins[$row['away']] = 0;
		}
                if (array_key_exists($row['away'], $losses)){
                        $losses[$row['away']] += 1;
                }else{
                        $losses[$row['away']] = 1;
                }
                if (!array_key_exists($row['home'], $losses)){
                        $losses[$row['home']] = 0;
                }


	}else{
                if (array_key_exists($row['away'], $wins)){
                        $wins[$row['away']] += 1;
                }else{
                        $wins[$row['away']] = 1;
                }
                if (!array_key_exists($row['away'], $wins)){
                        $wins[$row['home']] = 0;
                }
                if (array_key_exists($row['home'], $losses)){
                        $losses[$row['home']] += 1;
                }else{
                        $losses[$row['home']] = 1;
                }
                if (!array_key_exists($row['away'], $losses)){
                        $losses[$row['away']] = 0;
                }
	}
    }
}
asort($wins);
$wins = array_reverse($wins);
echo '<table id="standtable"><tr><th>Rank</th><th>Team</th><th>wins</th><th>losses</th></tr>';
$counter = 1;
foreach ($wins as $key => $value) {
	echo '<tr>';
	echo '<td>' . $counter . '</td>';
	echo '<td id="standtablename">' . $key . '</td>';
	echo '<td>' . $value . '</td>';
	echo '<td>' . $losses[$key] . '</td>';
	echo '</tr>';
	$counter += 1;
}
echo '</table>';
?>
