class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None
        self.prev = None
    def getData(self):
        return self.data
    def getNext(self):
        return self.next
    def setData(self,newdata):
        self.data = newdata
    def setNext(self,newnext):
        self.next = newnext
    def setPrev(self,newprev):
        self.prev = newprev
        

#作者：北京大学 郭炜  版权所有 未经授权不得复制 copyright：Guo Wei, Peking University
#程序来自中国水利水电出版社《数据结构与算法(Python语言实现)》教材(作者：郭炜)
#程序在书中有详细注释和讲解

class DoubleLinkList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
  
    def insert(self,p,data):
        nd = Node(data)
        if self.head == None:
            self.head = nd
            self.tail = nd
        else:
            nd.setPrev(p)
            nd.setNext(p.next)

            if self.tail is p:  
                self.tail = nd
            if p.next:
                p.next.setPrev(nd)
            p.next = nd
        self.size += 1
    def remove(self,p):  
        if self.size == 0 or p is self.head:
            raise Exception("Illegal deleting.")
        else:
            p.prev.setNext(p.next)
            if p.next: 
                p.next.setPrev(p.prev)
            if self.tail is p:
                self.tail = p.prev
            self.size -= 1
    
    def search(self,item):
        current = self.head
        found= False
        stop = False
        while current != None and not found and not stop:
            if current.getData()== item:
                found = True
                break
            else:
                if current.getData()> item:
                    stop = True
                else:
                    current = current.getNext()
        return current
    
    def pushFront(self,data): 
        self.insert(self.head,data)
    
    def pushBack(self,data):
        self.insert(self.tail,data)
	# def clear(self):
	# 	self._tail = self._head
	# 	self._head.next = self._head.prev = None
	# 	self._size = 0
	# def begin(self):
	# 	return DoubleLinkList._Iterator(self._head.next)
	# def end(self):
	# 	return None
	# def insert(self,i,data): 
	# 	self._insert(i.ptr,data)
	# def delete(self, i):  
	# 	self._delete(i.ptr)

	# def popFront(self):
	# 	self._delete(self._head.next)

	# def popBack(self):
	# 	self._delete(self._tail)
	# def __iter__(self):
	# 	self.ptr = self._head.next
	# 	return self
	# def __next__(self):
	# 	if self.ptr is None:
	# 		raise StopIteration()  
	# 	else:
	# 		data = self.ptr.data
	# 		self.ptr = self.ptr.next
	# 		return data
	# def find(self ,val): 
	# 	ptr = self._head.next
	# 	while ptr is not None:
	# 		if ptr.data == val:
	# 			return DoubleLinkList._Iterator(ptr)
	# 		ptr = ptr.next
	# 	return self.end()
	# def printList(self):
	# 	ptr = self._head.next
	# 	while ptr is not None:
	# 		print(ptr.data,end=",")
	# 		ptr = ptr.next

linkLst = DoubleLinkList()
for i in range(5):
	linkLst.pushBack(i)
# i = linkLst.begin()
# while i != linkLst.end(): 
# 	print(i.getData(),end = ",")
# 	i = next(i)
# print()
i = linkLst.search(3)
i.setData(300)
# linkLst.printList()  
print()
linkLst.insert(i,6000) 
# linkLst.printList() 
print()
linkLst.remove(i)
# linkLst.printList() 
