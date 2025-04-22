from tree1 import Tree

class BinaryTree:
	def __init__(self,data,left = None,right = None):
		self.data,self.left,self.right = data,left,right
	def addLeft(self,tree): #tree是一个二叉树
		self.left = tree
	def addRight(self,tree): #tree是一个二叉树
		self.right = tree


def treeToBinaryTree(tree):
#直观表示法的树转儿子兄弟树。tree是Tree对象
	bTree = BinaryTree(tree.data) #二叉树讲义中的BinaryTree
	for i in range(len(tree.subtrees)):
		if i == 0:
			tmpTree = treeToBinaryTree(tree.subtrees[i])
			bTree.addLeft(tmpTree)
		else:
			tmpTree.addRight(treeToBinaryTree(tree.subtrees[i]))
			tmpTree = tmpTree.right
	return bTree

def binaryTreeToTree(biTree):
#儿子兄弟树转直观表示法的树转。biTree是BinaryTree对象
	tree = Tree(biTree.data)
	son = biTree.left
	if son:
		tree.addSubTree(binaryTreeToTree(son))
		while son.right:
			tree.addSubTree(binaryTreeToTree(son.right))
			son = son.right
	return tree
