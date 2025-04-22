def heapSort(a,key = lambda x:x): #对列表a进行排序
    def makeHeap(): #建堆
        i = (heapSize - 1 - 1) // 2 #i是最后一个叶子的父亲
        for k in range(i,-1,-1):
            shiftDown(k)
    def shiftDown(i): #a[i]下移
        while i * 2 + 1 < heapSize:  #只要a[i]有儿子就做
            L,R = i * 2 + 1, i * 2 + 2
            if R >= heapSize or key(a[L]) < key(a[R]):
                s = L
            else:
                s = R
            if key(a[s]) < key(a[i]):
                a[i],a[s] = a[s],a[i]
                i = s
            else:
                break

    heapSize = len(a)
    makeHeap()
    for i in range(len(a)-1,0,-1):
        a[i],a[0] = a[0],a[i]
        heapSize -= 1
        shiftDown(0)
    n = len(a)
    for i in range(n//2): #颠倒a
        a[i],a[n-1-i] = a[n-1-i],a[i]

a = [3,21,4,76,12,3]
heapSort(a)
print(a) #>>[3, 3, 4, 12, 21, 76]
