def sortedSquaredArray(array) :
    newArr = []
	for num in array:
		newArr.append(num * num)
	newArr.sort()
	return newArr
# O(nlogn) time | O(1) space

