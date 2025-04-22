class Tree:
    def __init__(self,data, *subtrees): #参数个数可变的函数
        #参数subtrees是个元组，其中每个元素都是一个Tree对象
        self.data = data
        self.subtrees = list(subtrees) #self.subtrees是子树列表
    def addSubTree(self,tree): #tree是一个Tree对象
        self.subtrees.append(tree)
    def preorderTraversal(self,op):
        op(self)
        for t in self.subtrees:
            t.preorderTraversal(op)
    def postorderTraversal(self,op):
        for t in self.subtrees:
            t.postorderTraversal(op)
        op(self)

    def printTree(self,level = 0): #输出树的层次结构
        print("\t" * level + str(self.data))
        for t in self.subtrees:
            t.printTree(level+1)



nodes = []

nodesPtr = 0  #表示看到nodes里的第几行

def buildTree(level): #读取nodesPtr指向的那一行，并建立以其为根的子树
	#该根的层次是level。建好后，令nodesPtr指向该子树的下一行
	global nodesPtr,nodes
	tree = Tree(nodes[nodesPtr][1]) #建根结点
	nodesPtr += 1 #看下一行
	while nodesPtr < len(nodes) and nodes[nodesPtr][0] == level + 1:
		tree.addSubTree(buildTree(level + 1))
	return tree


while True:
	try:
		s = input().rstrip()
		nodes.append((len(s)-1,s.strip()))
	except:
		break

print(nodes)
tree = buildTree(0)


