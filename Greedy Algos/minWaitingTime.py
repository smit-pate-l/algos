def minimumWaitingTime(queries):
	queries.sort()
	currentWaitingTime,totalWaitingTime = 0, 0
	for time in range(0,len(queries) - 1):
		currentWaitingTime += queries[time]
		totalWaitingTime += currentWaitingTime
    return totalWaitingTime