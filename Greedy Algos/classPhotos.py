def classPhotos(redShirtHeights, blueShirtHeights):
	redShirtHeights.sort()
	blueShirtHeights.sort()
	
	frontRow = 'red' if blueShirtHeights[0] > redShirtHeights[0] else 'blue'
	for idx in range(len(blueShirtHeights)):
		blueShirtHeight = blueShirtHeights[idx]
		redShirtHeight = redShirtHeights[idx]
		
		if frontRow == 'red':
			if redShirtHeight >= blueShirtHeight:
				return False
		else:
			if redShirtHeight <= blueShirtHeight:
				return False
			
    return True

