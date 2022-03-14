def minimumWaitingTime(queries):
	queries.sort()
	currentWaitingTime,totalWaitingTime = 0, 0
	for time in range(0,len(queries) - 1):
		currentWaitingTime += queries[time]
		totalWaitingTime += currentWaitingTime
    return totalWaitingTime
#O(nlogn) time | O(1) space

def minimumWaitingTime(queries):
	queries.sort()
	
	totalWaitingTime = 0
	for idx, duration in enumerate(queries):
		queriesLeft = len(queries) - (idx + 1)
		totalWaitingTime += duration * queriesLeft
	return totalWaitingTime
#O(nlogn) time | O(1) space
