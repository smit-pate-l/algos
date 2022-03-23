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