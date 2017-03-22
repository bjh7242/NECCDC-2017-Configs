<?php
include("common.php");
$sql = "SELECT scores.uid, scores.score, users.username, users.uid FROM scores INNER JOIN users ON scores.uid=users.uid ORDER BY scores.score";
$data = "";
if($result = $link->query($sql)){
    while ($row = $result->fetch_assoc()) {
        $data .= '<tr><td>'.$row['username'] . '</td><td>'.$row['score'].'</td></tr>';
    }
}
?>

<div id="content">
<h1>Top 10 Players</h1>
<center><div id="rankings"><table id="ranktable"><tr><th>username</th><th>score</th></tr><?php echo $data; ?></table></div></center>
<br />
</div>
