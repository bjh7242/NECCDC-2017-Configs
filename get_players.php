<?php
include("common.php");
$sql = "Select appearances.playerID, master.playerID, master.weight, master.height, master.bats, master.throws, master.nameLast, master.nameFirst from appearances INNER JOIN master ON appearances.playerID=master.playerID where yearID=2015";
$years = array();
$y = array("data"=>array());
if($result = $link3->query($sql)){
    while ($row = $result->fetch_assoc()) {
	$m = array($row["playerID"],$row["nameFirst"],$row["nameLast"],$row["weight"],$row["height"],$row["bats"],$row["throws"]);
	array_push($y['data'],$m);

    }
}
$out = json_encode($y);
echo $out;

?>

