def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
	total = 0
    if fastest == True:
		redShirtSpeeds.sort()
		blueShirtSpeeds.sort(reverse = True)
	else:
		redShirtSpeeds.sort()
		blueShirtSpeeds.sort()

	for idx in range(len(blueShirtSpeeds)):
		total += max(blueShirtSpeeds[idx], redShirtSpeeds[idx])

    return total


def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
	total = 0
    redShirtSpeeds.sort()
	blueShirtSpeeds.sort()
	if fastest == True:
		reverseArrayInPlace(redShirtSpeeds)
		

	for idx in range(len(blueShirtSpeeds)):
		total += max(blueShirtSpeeds[idx], redShirtSpeeds[idx])

    return total

def reverseArrayInPlace(array):
	start = 0
	end = len(array) - 1
	
	while start < end:
		array[start], array[end] = array[end], array[start]
		start += 1
		end -= 1