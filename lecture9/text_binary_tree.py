from tree_expression import BinaryTree

def buildTree(nodes):
    nodesPtr = 0  #正要看nodes里的第几个元素
    def build(level):
        #读取nodesPtr指向的那一个元素，并建立以其为根的子树，该根的层次是level。
        nonlocal nodesPtr
        tree = BinaryTree(nodes[nodesPtr][1]) #建根结点
        nodesPtr += 1 #看下一个元素
        if nodesPtr < len(nodes) and nodes[nodesPtr][0] == level + 1:
            if nodes[nodesPtr][1] != '0':
                tree.insertLeft(build(level + 1))
            else:  #没有左子树
                nodesPtr += 1
        if nodesPtr < len(nodes) and nodes[nodesPtr][0] == level + 1:
            tree.insertRight(build(level + 1))
        return tree
    return build(0)


#build会推进nodesPtr到文本中所建的子树的下一行的位置
nodes = [] #nodes元素为 (缩进，数据)，例如：[(0, 'A'), (1, 'B'), ......]
             #每个元素代表一个结点，缩进即结点的层次
# nodes=[(0,A), (1,B), (2,0), (2,D), (3,E), (1,F), (2,G), (3,I), (3,J), (2,H)]
nodes=[(0, 'A'), (1, 'B'), (2, '0'), (2, 'D'), (3, 'E'), (1, 'F'), (2, 'G'), (3, 'I'), (3, 'J'), (2, 'H')]

# nodes = sorted(nodes, key=lambda x: x[0])  # 按照缩进排序

tree = buildTree(nodes)

print()


# while True:
# 	try:
# 		s = input().rstrip()
# 		nodes.append((len(s)-1,s.strip()))
# 	except:
# 		break

