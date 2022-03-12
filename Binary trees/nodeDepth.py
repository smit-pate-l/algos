def nodeDepths(node, depth = 0):
    # Write your code here.
	if node is None:
		return 0
	return depth + nodeDepths(node.left, depth + 1) + nodeDepths(node.right, depth + 1)
  


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

#Solution 2 (BFS)

def nodeDepths(root):
	sum = 0
	queue = [{'node': root, 'depth': 0}]
	while len(queue) > 0:
		nodeInfo = queue.pop()
		node, depth = nodeInfo['node'], nodeInfo['depth']
		if node is None:
			continue
		sum += depth
		queue.append({'node':node.left, 'depth': depth + 1})
		queue.append({'node':node.right, 'depth': depth + 1})
	return sum

# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

#O(n) time | O(h) space where n = number of nodes in binary tree & h = heoght of the binary tree (in both solutions)
