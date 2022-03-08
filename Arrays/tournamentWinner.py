def tournamentWinner(competitions, results):
    currentBest = ""
	teams = {currentBest:0}
	
	for idx, competition in enumerate(competitions):
		homeTeam, awayTeam = competition
		result = results[idx]
		
		winningTeam = homeTeam if result == 1 else awayTeam
		
		updateScore(winningTeam,3, teams)
			
		if teams[currentBest] < teams[winningTeam]:
			currentBest = winningTeam			
    return currentBest

def updateScore (team, points, teams):
	if team not in teams:
		teams[team] = 0
		
	teams[team] += points