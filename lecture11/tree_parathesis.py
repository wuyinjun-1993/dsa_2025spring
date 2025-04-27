#作者：北京大学 郭炜  版权所有 未经授权不得复制 copyright：Guo Wei, Peking University
#程序来自中国水利水电出版社《数据结构与算法(Python语言实现)》教材(作者：郭炜)
#程序在书中有详细注释和讲解

class Tree:
	def __init__(self,data):
		self.data = data
		self.subtrees = []
	def addSubTree(self,tree): 
		self.subtrees.append(tree)
	def preorderTraversal(self,op):
		op(self)
		for t in self.subtrees:
			t.preorderTraversal(op)
	def postorderTraversal(self,op):
		for t in self.subtrees:
			t.postorderTraversal(op)
		op(self)
	def bfsTraversal(self,op): 
		import collections
		dq = collections.deque()
		dq.append(self)
		while len(dq) > 0:
			nd = dq.popleft()
			op(nd)
			for x in nd.subtrees:
				dq.append(x)

def buildTree(treeString):
    ptr = 0
    def build():
        nonlocal ptr 
        data = treeString[ptr]
        tree = Tree(data)  
        ptr += 1 
        if ptr == len(treeString):
            return tree  
        if treeString[ptr] == '(': 
            ptr += 1
            tree.addSubTree(build())
            while  treeString[ptr] == ',':
                ptr += 1 
                tree.addSubTree(build())
            ptr += 1 
        return tree
    return build()

treeString = input()
tree = buildTree(treeString)
tree.preorderTraversal(lambda x:print(x.data,end=""))
print()
tree.postorderTraversal(lambda x:print(x.data,end=""))





