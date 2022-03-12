closestVal = 0
def findClosestValueInBst(tree, target):
	global closestVal
	if tree is None:
		return closestVal
	if target > tree.value:
		if abs(target - closestVal) > abs(target-tree.value):
			closestVal = tree.value 
		findClosestValueInBst(tree.right, target)
	else:
		if abs(target - closestVal) > abs(target-tree.value):
			closestVal = tree.value 
		findClosestValueInBst(tree.left, target)
	return closestVal



# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None