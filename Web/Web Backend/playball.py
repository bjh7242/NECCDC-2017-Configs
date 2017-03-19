import datetime
import mysql.connector
import sys
import random
import math
from numpy.random import choice
import argparse

parser = argparse.ArgumentParser(description='This is a PyMOTW sample program')
parser.add_argument('--year', action="store", dest="myyear", required=True)
result = parser.parse_args()

cnx = mysql.connector.connect(user='baseball', password='baseball', database='stats')
cursor = cnx.cursor()

def setup_teams():
	cnx2 = mysql.connector.connect(user='baseball', password='baseball', database='baseball')
	return [cnx2]

def query_teams(cursors,query):
	for cn in cursors:
		cur = cn.cursor()
		cur.execute(query)
		cn.commit()
cursors = setup_teams()
myyear = result.myyear
year = "2015"
query = ("SELECT DISTINCT teams.name,teams.park, teams.teamID FROM batting INNER JOIN teams on batting.teamID=teams.teamID where teams.yearID='"+year+"'")

cursor.execute(query)
num_games = 162
home_games = num_games/2
away_games = num_games - home_games
number_weeks = 26

teams = []
parks = []
teamID = []


for playerid in cursor:
  teams.append(playerid[0])
  parks.append(playerid[1])
  teamID.append(playerid[2])
  
def movePlayer(bases,move):
	score = 0
	if move == 1:
		if(bases[2] == 1):
			score += 1
			bases[2] = 0
		if(bases[1] == 1):
			bases[2] = 1
			bases[1] = 0
		if(bases[0] == 1):
			bases[1] = 1
			bases[0] = 0
		bases[0] = 1
	if move == 2:
		if(bases[2] == 1):
			score += 1
			bases[2] = 0
		if(bases[1] == 1):
			score += 1
			bases[1] = 0
		if(bases[0] == 1):
			bases[2] = 1
			bases[0] = 0
		bases[1] = 1
	if move == 3:
		if(bases[2] == 1):
			score += 1
			bases[2] = 0
		if(bases[1] == 1):
			score += 1
			bases[1] = 0
		if(bases[0] == 1):
			score += 1
			bases[0] = 0
		bases[2] = 1
	if move == 4:
		if(bases[2] == 1):
			score += 1
			bases[2] = 0
		if(bases[1] == 1):
			score += 1
			bases[1] = 0
		if(bases[0] == 1):
			score += 1
			bases[0] = 0
		bases[1] = 0
		score += 1
	return bases,score
		
  
def getData(team, year):
	# Get all players for away team #lazy
	query = ("SELECT DISTINCT master.nameFirst, master.nameLast, batting.playerID FROM master INNER JOIN batting on batting.playerID=master.playerID where batting.teamID='"+ team +"' AND batting.yearID='"+year+"' ORDER BY batting.G DESC")
	cursor.execute(query)
	names = []
	playerids = []
	for playerinfo in cursor:
			names.append(playerinfo[0] + " " + playerinfo[1])
			playerids.append(playerinfo[2])
	# pick whose playing
	positions_needed = [['C',2],['1B',2],['2B',2],['3B',2],['SS',2],['RF',2],['LF',2],['CF',2],['P',9]]
	query = ("SELECT DISTINCT batting.playerID, fielding.POS, batting.G, batting.AB, batting.H, batting.2B, batting.3B, batting.HR, batting.SO, batting.BB FROM fielding INNER JOIN batting on batting.playerID=fielding.playerID where batting.teamID='"+ team +"' AND batting.yearID='"+year+"' GROUP BY batting.playerID ORDER BY batting.G DESC")
	cursor.execute(query)
	player_positions = []
	player_games_played = []
	player_atbats = []
	player_singles  = []
	player_doubles = []
	player_triples = []
	player_homeruns = []
	player_strikeouts = []
	player_walks = []
	player_hits = []
	for playerinfo in cursor:
		player_positions.append(playerinfo[1])
		player_games_played.append(playerinfo[2])
		player_atbats.append(playerinfo[3])
		player_singles.append(playerinfo[4])
		player_doubles.append(playerinfo[5])
		player_triples.append(playerinfo[6])
		player_homeruns.append(playerinfo[7])
		player_strikeouts.append(playerinfo[8])
		player_walks.append(playerinfo[9])
		player_hits.append(playerinfo[4]+playerinfo[5]+playerinfo[6]+playerinfo[7])
	# pick who will play
	lineup = []
	for player in range(0,len(names)-1):
		prob_play = math.ceil((player_games_played[player]*1.0/num_games)*100)
		prob_rand = random.randint(1,100)
		# if they have the right probability
		if prob_rand <= int(prob_play):
			# check if they play the right position
			for i in range(0,len(positions_needed)):
				# if we're looking for an outfielder... we need to check for OF
				if positions_needed[i][0] == "RF" or positions_needed[i][0] == "LF" or positions_needed[i][0] == "CF":
					# if the player is an OF we're also good
					if player_positions[player] == "OF":
						if positions_needed[i][1] > 0:
							positions_needed[i][1] -= 1
							lineup.append(player)					
							break
				# otherwise check for our actual position
				if positions_needed[i][0] == player_positions[player]:
					if positions_needed[i][1] > 0:
						positions_needed[i][1] -= 1
						lineup.append(player)
	for i in positions_needed:
		remain = set() 
		iter = 0
		while i[1] != 0:
			#pick a random player and see if they are that position
			rand_player = random.randint(0,len(player_positions)-1)
			if rand_player in lineup:
				continue
			else:
				# if we've gone through 100 times already then you know just add a random guy
				if iter > 100:
					i[1] -= 1
					lineup.append(rand_player)
					iter = 0
				# if we have the right type of player add them
				if player_positions[rand_player] == i[0]:
					i[1] -= 1
					lineup.append(rand_player)
					iter = 0
			iter += 1
	# order our lineup by best AB%
	# generate AB%
	player_hitperc = []
	for i in range(0,len(names)-1):
		if player_atbats[i] == 0 or player_hits[i] == 0:
			player_hitperc.append(random.randint(0,8))
		else:
			# only use hitting if we have a large enough sample
			if player_atbats[i] > 80: 
				 player_hitperc.append((player_hits[i]*1.0/player_atbats[i]*1.0)*100)
			else:
				random.randint(8,15)
	return lineup, player_hitperc, playerids, player_singles, player_doubles, player_triples, player_homeruns, player_strikeouts,player_walks, player_atbats, names

  
max_games_against = num_games/len(teams)

games_left = [num_games]*len(teams)
home_games_left = [home_games]*len(teams)
games = []
for team in range(0,len(games_left)):
	# we'll break down to an odd number sometimes catch that
	repeats = 0
	while(games_left[team] != 0):
		repeats += 1
		# We default to playing at home
		home = True
		if repeats > 1000:
			break
		# bypass checks if we have gone round 100 times
		while repeats>100:
			most_games = 0
			most_games_index = -1
			for i in range(0,len(games_left)):
				if i == team:
					continue
				if games_left[i] > most_games:
					most_games = games_left[i]
					most_games_index = i
			if most_games_index == -1:
				break
			if games_left[team] == 0 or games_left[team_2_play] == 0:
				break
			game = (team,team_2_play)
			games_left[team] -= 1
			games_left[team_2_play] -= 1
			games.append(game)			
		# if we got to the last team and there are still left we're not good
		if team == 29:
			break
		# Pick a random team to play (we go in order to we optimize)
		team_2_play = random.randint(team+1, len(teams)-1)
		# if we picked ourselves keep going
		if team_2_play == team:
			continue
		# if the team we picked has no games left keep going
		if games_left[team_2_play] == 0:
			continue
		# generate the game
		game = (team,team_2_play)
		# If we have no more home games play at others house
		if home_games_left[team] == 0:
			if home_games_left[team_2_play] > 0:
				# Switch the game to be at their house
				game = (team_2_play,team)
				home = False
			else:
				# We have to keep picking both teams are out of home games
				continue
		else:
			# Check to see if we have played against that team the max amount
			altgame = (game[1],game[0])
			count = 0
			for i in games:
				if i == game:
					count+=1
				if i == altgame:
					count+=1
			# We played too many games against that team
			# exception if we can't do that anymore
			if(repeats<100):
				if count > max_games_against:
					continue
				
				
			# if we're not home make sure to subtract from them
			if home==False:
				home_games_left[team_2_play] -= 1
			else:
				# We found a home game to play
				home_games_left[team] -= 1
		games_left[team] -= 1
		games_left[team_2_play] -= 1
		repeats = 0
		games.append(game)
# randomize the schedule we generated
random.shuffle(games)

def player_bats(index_at_bat,stats):
	walks = stats[8][index_at_bat]
	atbats = stats[9][index_at_bat]
	strikeouts = stats[7][index_at_bat]
	singles = stats[3][index_at_bat]
	doubles = stats[4][index_at_bat]
	triples = stats[5][index_at_bat]
	hrs = stats[6][index_at_bat]
	if singles == 0:
		singles = random.randint(0,20)*1.0/100
		atbats += 1
	if doubles == 0:
		doubles = random.randint(0,20)*1.0/100
		atbats += 1
	if triples == 0:
		triples = random.randint(0,20)*1.0/100
		atbats += 1
	if hrs == 0:
		hrs = random.randint(0,20)*1.0/100
		atbats += 1
	if walks == 0:
		walks = random.randint(0,20)*1.0/100
		atbats += 1
	if strikeouts == 0:
		strikeouts = random.randint(0,30)*1.0/100
		atbats += 1
	if atbats == 0:
		atbats = 1
	walkpct = walks/float(atbats)
	strikeoutpct = strikeouts/float(atbats)
	singlepct = singles/float(atbats)
	doublepct = doubles/float(atbats)
	triplepct = triples/float(atbats)
	hrpct = hrs/float(atbats)
	outpct = 1 - (hrpct + triplepct+doublepct+singlepct+strikeoutpct+walkpct)
	elements = ['ball', 'strike', 'single','double','triple','homerun','out']
	if outpct < 0:
		outpct = 0
	weights = [walkpct,strikeoutpct,singlepct,doublepct,triplepct,hrpct,outpct]
	summ = 0
	for i in weights:
		summ += i
	if summ > 1:
		remove = summ - 1
	else:
		remove = 0
	while remove != 0:
		w = random.randint(0,len(weights)-1)
		amount_removed = remove/2.0
		if amount_removed < 0.1:
			amount_removed = remove
		if (weights[w] - amount_removed) > 0:
			weights[w] -= amount_removed
			remove -= amount_removed
		else:
			pass
	summ = 0
	for i in weights:
		summ+=i
	outcome = choice(elements, p=weights)
	return outcome
	
# Loop through each game
counter = 0
for i in games:
	counter +=1
	# List whose playing
	print teams[i[0]], "at", teams[i[1]], "playing at", parks[i[0]]
	team = teamID[i[0]]
	alt_team = teamID[i[1]]
	home_lineup, home_player_hitperc, home_playerids, h_singles, h_doubles, h_triples, h_homeruns, h_strikeouts, h_walks, h_player_atbats, h_names = getData(team, year)
	homeStats = [home_lineup, home_player_hitperc, home_playerids, h_singles, h_doubles, h_triples, h_homeruns, h_strikeouts, h_walks, h_player_atbats, h_names]
	
	away_lineup, away_player_hitperc, away_playerids, a_singles, a_doubles, a_triples, a_homeruns, a_strikeouts, a_walks,a_atbats,a_names = getData(team, year)
	awayStats = [away_lineup, away_player_hitperc, away_playerids, a_singles, a_doubles, a_triples, a_homeruns, a_strikeouts, a_walks,a_atbats, a_names]
	
	# Play the game:
	location_in_home_lineup = 0
	location_in_away_lineup = 0
	inning = 1
	team_batting = "away"
	outs = 0
	home_score = 0
	away_score = 0
	strikes = 0
	balls = 0
	half_of_inning = 0
	game_is_going = True
	bases = [0,0,0]
	# TODO: pick a random pitcher
	
	while game_is_going:
		# throw a pitch
		if team_batting == "away":
			index_at_bat = away_lineup[location_in_away_lineup]
			pitch = player_bats(index_at_bat,awayStats)
		if team_batting == "home":
			index_at_bat = home_lineup[location_in_home_lineup]
			pitch = player_bats(index_at_bat,homeStats)

		if pitch=='single':
			if team_batting == "home":
				location_in_home_lineup += 1
				location_in_home_lineup %= (len(home_lineup))
				bases, score = movePlayer(bases,1)
				home_score += score
				print "\t " + str(homeStats[10][index_at_bat]) + " hits a single", bases
			if team_batting == "away":
				location_in_away_lineup += 1
				location_in_away_lineup %= (len(away_lineup))
				bases, score = movePlayer(bases,1)
				away_score += score
				print "\t " + str(awayStats[10][index_at_bat]) + " hits a single", bases
		if pitch=='double':
			if team_batting == "home":
				location_in_home_lineup += 1
				location_in_home_lineup %= (len(home_lineup))
				bases, score = movePlayer(bases,2)
				home_score += score
				print "\t" + str(homeStats[10][index_at_bat]) + " hits a double", bases
			if team_batting == "away":
				location_in_away_lineup += 1
				location_in_away_lineup %= (len(away_lineup))
				bases, score = movePlayer(bases,2)
				away_score += score
				print "\t" + str(awayStats[10][index_at_bat]) + " hits a double", bases
		if pitch=='triple':
			if team_batting == "home":
				location_in_home_lineup += 1
				location_in_home_lineup %= (len(home_lineup))
				bases, score = movePlayer(bases,3)
				print "\t" + str(homeStats[10][index_at_bat]) + " hits a triple", bases
				home_score += score
			if team_batting == "away":
				location_in_away_lineup += 1
				location_in_away_lineup %= (len(away_lineup))
				bases, score = movePlayer(bases,3)
				away_score += score
				print "\t" + str(awayStats[10][index_at_bat]) + " hits a triple", bases
		if pitch=='homerun':
			if team_batting == "home":
				location_in_home_lineup += 1
				location_in_home_lineup %= (len(home_lineup))
				bases, score = movePlayer(bases,4)
				print "\t" + str(homeStats[10][index_at_bat]) + " hits a HOMERUN", bases
				home_score += score
			if team_batting == "away":
				location_in_away_lineup += 1
				location_in_away_lineup %= (len(away_lineup))
				bases, score = movePlayer(bases,4)
				print "\t" + str(awayStats[10][index_at_bat]) + " hits a HOMERUN", bases
				away_score += score	
		if pitch == "ball":
			balls = 4
		if pitch == "strike":
			strikes = 3
		if balls == 4:
			balls = 0
			strikes = 0
			if team_batting == "home":
				location_in_home_lineup += 1
				location_in_home_lineup %= (len(home_lineup))
				bases, score = movePlayer(bases,1)
				home_score += score
			if team_batting == "away":
				location_in_away_lineup += 1
				location_in_away_lineup %= (len(away_lineup))
				bases, score = movePlayer(bases,1)
				away_score += score
			print "\twalk",bases
		if strikes == 3 or pitch == "out":
			outs +=1
			if strikes == 3:
				print "\tstruck out",bases
			if pitch == "out":
				print "\tpop/ground out",bases
			if team_batting == "home":
				location_in_home_lineup += 1
				location_in_home_lineup %= (len(home_lineup))
			if team_batting == "away":
				location_in_away_lineup += 1
				location_in_away_lineup %= (len(away_lineup))
			balls = 0
			strikes = 0	
		if outs == 3:
			print "3 outs" ,str(inning) + "/" + str(half_of_inning) + " - " + str(home_score) + ":" + str(away_score)
			# Stop the game if we're done
			if inning == 9 and half_of_inning == 1 and outs == 3 and home_score != away_score:
				game_is_going = False
				query = "INSERT INTO `games` (`gamenum`, `home`, `away`, `hscore`, `ascore`, `loc`, `innings`,`year`) VALUES ("+str(counter)+", '"+ teams[i[0]]+"', '"+teams[i[1]]+"', "+str(home_score)+", "+str(away_score)+", '"+parks[i[0]]+"', "+str(inning)+", "+str(myyear)+")"
				query_teams(cursors,query)
				print "HOME SCORE ", home_score, " - AWAY SCORE ", away_score
			if inning > 9 and half_of_inning == 1 and outs == 3 and home_score != away_score:
				game_is_going = False
				query = "INSERT INTO `games` (`gamenum`, `home`, `away`, `hscore`, `ascore`, `loc`, `innings`,`year`) VALUES ("+str(counter)+", '"+ teams[i[0]]+"', '"+teams[i[1]]+"', "+str(home_score)+", "+str(away_score)+", '"+parks[i[0]]+"', "+str(inning)+", "+str(myyear)+")"
                                query_teams(cursors,query)
				print "HOME SCORE ", home_score, " - AWAY SCORE ", away_score
			bases = [0,0,0]
			balls = 0
			strikes = 0
			outs = 0
			if half_of_inning == 0:
				half_of_inning = 1
			elif half_of_inning == 1:
				half_of_inning = 0
				inning += 1
			if team_batting == "away":
				team_batting = "home"
			if team_batting == "home":
				team_batting == "away"

		
	
		
		#for z in updated_lineup
		#	print 
		
	#print positions_needed
	#print len(lineup)
	#for i in lineup:
	#	print names[i],
	#	print " ", player_positions[i]
	# pick the remaining members at random
		
	#print len(home_names)
	#print len(names)
	#print len(player_positions)
	#sys.exit()
# get all the players
#for i in 
cursor.close()
cnx.close()
for i in cursors:
	i.close()
cnx2.close()
