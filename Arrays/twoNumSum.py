def twoNumberSum(array, targetSum):
    nums = {}
    for num in array:
	    expectedSum = targetSum - num
        if expectedSum in nums:
		    return [expectedSum,num]
        else:
			nums[num] = True
	return []
# O(n^2) time | O(1) space

def twoNumberSum(array, targetSum):
    array.sort()
    left = 0
    right = len(array) - 1
    while left < right:
        currentSum = array[left] + array[right]
        if currentSum == targetSum:
            return [array[left], array[right]]
        elif currentSum < targetSum:
            left += 1
        elif currentSum > targetSum:
            right -= 1
    return []
# O(nlogn) time | O(1) space

def twoNumSum(array, targetSum) :
    nums = {}
    for num in array:
        potentialMatch = targetSum - num
        if potentialMatch in nums :
            return [potentialMatch, num]
        else:
            nums[num] = True
    return []
# O(n) time | O(n) space