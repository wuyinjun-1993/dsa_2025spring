class BinarysearchTree:
    def __init__ (self):
        self.root = None
        self.size= 0
    def length(self):
        return self.size
    def __len__(self):
        return self.size
    def __iter__(self):
        return self.root.__iter__()
    

class TreeNode:
    def __init__(self,key,val,left=None,\
        right=None,parent=None):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent
    def hasLeftchild(self):
        return self.leftChild
    def hasRightchild(self):
        return self.rightChild
    def isLeftchild(self):
        return self.parent and self.parent.leftChild == self
    def isRightchild(self):
        return self.parent and self.parent.rightChild == self
    def isRoot(self):
        return not self.parent
    def isLeaf(self):
        return not(self.rightChild or self.leftChild)
    def hasAnyChildren(self):
        return self.rightChild or self.leftChild
    def hasBothchildren(self):
        return self.rightChild and self.leftChild
    def replaceNodeData(self,key,value,lc,rc):
        self.key = key
        self.payload = value
        self.leftChild=lc
        self.rightChild=rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self
            
    def put(self,key,val):
        if self.root :
            self. _put(key,val,self.root)
        else:
            self.root = TreeNode(key,val)
            
        self.size = self.size + 1
        
    def _put(self,key,val,currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftchild():
                self._put(key,val,currentNode.leftChild)
            else:
                currentNode.leftChild =TreeNode(key,val,parent=currentNode)
        else:
            if currentNode.hasRightchild():
                self._put(key,val,currentNode.rightchild)
            else:
                currentNode.rightChild =TreeNode(key,val,parent=currentNode)
                
                
    def __setitem__(self,k,v):
        self.put(k,v)
        

    def get(self,key):
        if self.root:
            res = self._get(key,self.root)
            if res:
                return res.payload
            else:
                return None
        else:
            return None
        
    def _get(self,key,currentNode):
        if not currentNode:
            return None
        elif currentNode.key == key:
            return currentNode
        elif key < currentNode.key:
            return self._get(key,currentNode.leftchild)
        else:
            return self._get(key,currentNode.rightchild)
        
    
    def __getitem__(self,k):
        return self.get(k)
    
    def __contains__(self,k):
        if self._get(k,self.root):
            return True
        else:
            return False
        
        
    def _iter_(self):
        if self:
            if self.hasLeftChild():
                for elem in self.leftChild:
                    yield elem
            yield self.key
            if self.hasRightChild():
                for elem in self.rightChild:
                    yield elem
                    
    def delete(self,key):
        if self.size >1:
            nodeToRemove = self._get(key,self.root)
            if nodeToRemove:
                self.remove(nodeToRemove)
                self.size = self.size-1
            else:
                raise KeyError("Error, key not in tree")
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size= self.size-1
        else:
            raise KeyError('Error, key not in tree')
        
    def __delete__(self,key):
        self.delete(key)
    
    
    def findsuccessor(self):
        succ = None
        if self.hasRightchild():
            succ = self.rightChild.findMin()
        else:
            if self.parent:
                if self.isLeftchild():
                    succ = self.parent
                else:
                    self.parent.rightChild = None
                    succ = self.parent.findSuccessor()
                    self.parent.rightChild= self
        return succ
    
    def findMin(self):
        current = self
        while current.hasLeftChild():
            current = current.leftChild
            return current
    
    def spliceout(self):
        if self.isLeaf():
            if self.isLeftchild():
                self.parent.leftChild = None
            else:
                self.parent.rightChild = None
        elif self.hasAnyChildren():
            if self.hasLeftChild():
                if self.isLeftChild():
                    self.parent.leftChild = self.leftChild
                else:
                    self.parent.rightChild = self.leftChild
                self.leftChild.parent = self.parent
            else:
                if self.isLeftchild():
                    self.parent.leftChild = self.rightChild
                else:
                    self.parent.rightChild = self.rightChild
                self.rightChild.parent = self.parent
    
    def remove(self, currentNode):
            
        if currentNode.isLeaf():#leaf
            if currentNode == currentNode.parent.leftChild:
                currentNode.parent.leftChild = None
            else:
                currentNode.parent.rightChild = None
                
        elif currentNode.hasBothChildren():#interior
            succ = currentNode.findsuccessor()
            succ.spliceOut()
            currentNode.key = succ.key
            currentNode.payload = succ.payload
        
        
        else:# this node has one child
            if currentNode.hasLeftChild():
                if currentNode.isLeftChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.leftChild
                elif currentNode.isRightChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.leftChild
                else:
                    currentNode.replaceNodeData(currentNode.leftChild.key,
                                                currentNode.leftChild.payload,
                                                currentNode.leftChild.leftChild,
                                                currentNode.leftChild.rightChild)
            else:
                if currentNode.isLeftChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.rightChild
                elif currentNode.isRightChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.rightChild

                else:

                    currentNode.replaceNodeData(currentNode.rightChild.key,
                                                currentNode.rightChild.payload,
                                                currentNode.rightChild.leftchild,
                                                currentNode.rightChild.rightchild)
                    
                    