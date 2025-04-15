
class BinaryTree:
    def __init__(self,rootobj):
        self.key = rootobj
        self.leftChild = None
        self.rightChild = None
        
    def insertLeft(self,newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t= BinaryTree(newNode)
            t.leftChild= self.leftChild
            self.leftChild=t

    def insertRight(self,newNode):
        if self.rightChild == None:
            self.rightChild= BinaryTree(newNode)
        else:
            t= BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild=t
            
    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self,obj):
        self.key = obj

    def getRootVal(self):
        return self.key
    
    def preorder(self):
        print(self.key)
        if self.leftChild:
            self.leftChild.preorder()
        if self.rightChild:
            self.rightChild.preorder()

    def preorderTraversal(self):
        stack = [self]
        while len(stack) > 0:
            node = stack.pop()
            print(node.key)
            if node.right:
                stack.append(node.getRightChild())#先入栈的后访问，所以右子结点先入栈
            if node.left:
                stack.append(node.getLeftChild())  #后入栈的先访问，所以左子结点后入栈

    def inorderTravel(self):
        stack = [[self,0]] #0表示self的左子树还没有遍历过
        while len(stack) > 0:
            node = stack[-1]
            if node[0] == None: #node[0]是子树根结点
                stack.pop()
                continue
            if node[1] == 0: #左子树还没有遍历过
                stack.append([node[0].getLeftChild(),0])
                node[1] = 1 #表示node下次再出现在栈顶时左子树已经遍历过
            elif node[1] == 1: #左子树已经遍历过
                print(node[0].key)  
                stack.pop()
                stack.append([node[0].getRightChild(), 0])
                
                
