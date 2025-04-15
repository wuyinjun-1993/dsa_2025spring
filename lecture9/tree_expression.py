class Stack:
    def __init__(self):
        self.items =[]
    def isEmpty(self):
        return self.items ==[]
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)

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
            



def buildParseTree(fpexp):
    fplist = fpexp.split()
    pStack = Stack()
    eTree = BinaryTree('')
    pStack.push(eTree)
    currentTree =eTree
    for i in fplist:
        if i =='(':
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()
        elif i not in ['+','-','*','/',')']:
            currentTree.setRootVal(int(i))
            parent = pStack.pop()
            currentTree= parent
        elif i in ['+','-','*','/']:
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()
        elif i ==')':
            currentTree = pStack.pop()
        else:
            raise ValueError
    return eTree



import operator
def evaluate(parseTree):
    opers ={'+':operator.add,'-':operator.sub,\
        '*':operator.mul,'/':operator.truediv}
    
    leftC = parseTree.getLeftChild()
    rightC = parseTree.getRightChild()

    if leftC and rightC:
        fn = opers[parseTree.getRootVal()]
        return fn(evaluate(leftC),evaluate(rightC))
    else:
        return parseTree.getRootVal()
    
    
def preorder(tree):
    if tree:
        print(tree.getRootVal())
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())
    
def postorder(tree):
    if tree != None:
        postorder(tree.getLeftChild())
        postorder(tree.getRightChild())
        print(tree.getRootVal())

def inorder(tree):
    if tree != None:
        inorder(tree.getLeftChild())
        print(tree.getRootVal())
        inorder(tree.getRightChild())


def bfs(tree):
    if not tree:
        return
    queue = [tree]
    while queue:
        node = queue.pop(0)
        print(node.getRootVal())      # 访问当前节点
        if node.getLeftChild():
            queue.append(node.getLeftChild())
        if node.getRightChild():
            queue.append(node.getRightChild())




def postordereval(tree):
    opers ={'+':operator.add,'-':operator.sub,'*':operator.mul, '/':operator.truediv}
    res1 = None
    res2 = None
    if tree:
        res1 = postordereval(tree.getLeftChild())
        res2 = postordereval(tree.getRightChild())
        if res1 and res2:
            return opers[tree.getRootVal()](res1,res2)
        else:
            return tree.getRootVal()
        
        

