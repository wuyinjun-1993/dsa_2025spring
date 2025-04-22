
from binaryheap2 import BinHeap


def heapSort(a): #对列表a进行排序
    heap = BinHeap()
    heap.buildHeap(a) #将a变成一个堆
    # heapSize = len(a)
    n = len(heap.heapList)
    for i in range(len(heap.heapList)-1,0,-1):
        heap.heapList[i],heap.heapList[1] = heap.heapList[1],heap.heapList[i]
        heap.currentSize -= 1
        heap.percDown(1)
    
    for i in range(n//2): #颠倒a
        heap.heapList[i+1],heap.heapList[n-1-i] = heap.heapList[n-1-i],heap.heapList[i+1]
        
    return heap.heapList[1:] #返回排序后的列表，去掉第一个元素0

a = [3,21,4,76,12,3]
a = heapSort(a)
print(a) #>>[3, 3, 4, 12, 21, 76]

