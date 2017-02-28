<?php
include_once('common.php');
include_once('session');
$sql = "SELECT * FROM posts ORDER BY pid DESC limit 1";
if($result = $link->query($sql)){
	$row = $result->fetch_array(MYSQLI_ASSOC);
	$title = $row['title'];
	$post = $row['post'];
}else{
	$title = "Title N/A";
	$post = "Error: " . $link->error;
}
?>
<div id="content">
	<table>
	<tr>
	<td>
	<div id="news" class="box">
		<div id="news-header"><p class="headertext">Sports News</p></div>
		<h1><?php echo ucfirst($title); ?></h1>
		<?php echo ucfirst($post); ?>
	</div>
	</td>
	<td>
	<div id="standings" class="box">
		<div id="standings-header"><p class="headertext">Standings</p></div>
		<div id="standings-league">American</div>
		<table id="standings-table" border="0">
			<tr class="noborder">
				<th class="teamsize">Team</th>
				<th class="wltsize">W-L-T</th>
				<th class="pctsize">PCT</th>
			</tr>
			<tr>
				<td width="80%">Yankees</td>
				<td width="10%">8-6-9</td>
				<td>.900</td>
			</tr>
			<tr>
				<td>Yankees</td>
				<td>8-6-9</td>
				<td>.900</td>
			</tr>					
			<tr>
				<td>Yankees</td>
				<td>8-6-9</td>
				<td>.900</td>
			</tr>					
		</table>
	</div>
	</td>
	<td>
	<div id="scores" class="box">
		<div id="scores-header"><p class="headertext">Scores: Week 1</p></div>
		<table id="scores-table" border="0">
			<tr>
				<td class="fancy"><div id="test2">Yankees<p>10</p></div></td>
				<td  class="tablespace"> </td>
				<td rowspan="2" class="roundblack">Box</td>
				<td  class="tablespace"> </td>
				
			</tr>
			<tr>
				<td class="fancy">Red Socks<p>0</p></td>
			</tr>
			<tr><td colspan="4" class="divider"></td></tr>
			<tr>
				<td class="fancy"><div id="test2">Yankees<p>10</p></div></td>
				<td  class="tablespace"> </td>
				<td rowspan="2" class="roundblack">Box</td>
				<td  class="tablespace"> </td>
				
			</tr>
			<tr>
				<td class="fancy">Red Socks<p>0</p></td>
			</tr>				
		</table>
	</div>
	</td>
	</tr>
	</table>
</div>