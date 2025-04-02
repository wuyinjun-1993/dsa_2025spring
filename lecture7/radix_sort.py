
def radixSort(s, m, d, key):
    #key(x,k)可以取元素x的第k位原子
    for k in range(d):
        buckets = [[] for j in range(m)]
        for x in s:
            buckets[key(x, k)].append(x)
        i = 0
        for bkt in buckets: #这样收集复杂度O(len(s))
            for e in bkt:
                s[i] = e
                i += 1

def getKey(x, i):
    #取非负整数x的第i位。个位是第0位
    tmp = None
    for k in range(i + 1):
        tmp = x % 10
        x //= 10
    return tmp

lst = [123,21,48,745,143,62,269,87,300,6]
radixSort(lst, 10, 3, getKey)
print(lst) #>>[6, 21, 48, 62, 87, 123, 143, 269, 300, 745]

