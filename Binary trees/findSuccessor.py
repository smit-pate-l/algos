class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def findSuccessor(tree, node):
    treeOrder = inOrderTraversal(tree)
	
	for idx, currentNode in enumerate(treeOrder):
		if currentNode != node:
			continue
		if idx == len(treeOrder) - 1:
			return None
		return treeOrder[idx + 1]
    return None

def  inOrderTraversal(node, order = []):
	if node == None:
		return order
	inOrderTraversal(node.left)
	order.append(node)
	inOrderTraversal(node.right)
	
	return order
	