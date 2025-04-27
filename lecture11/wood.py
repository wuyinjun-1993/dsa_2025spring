
def woodsToBinaryTree(woods):
	#woods是个列表，每个元素都是一棵二叉树形式的树
	
	biTree = woods[0]
	p = biTree
	for i in range(1,len(woods)):
		p.addRight(woods[i])
		p = p.right
	return biTree
#biTree和woods共用结点,执行完后woods的元素不再是原儿子兄弟树


def binaryTreeToWoods(tree):
#tree是以二叉树形式表示的森林
	p = tree
	q = p.right
	p.right = None
	woods = [p]
	if q:
		woods += binaryTreeToWoods(q)
	return woods

