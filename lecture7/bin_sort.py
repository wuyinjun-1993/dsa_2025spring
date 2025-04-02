
def bucketSort(s,m,key=lambda x:x):
    buckets = [[] for i in range(m)]
    for x in s:
        buckets[key(x)].append(x)
    i = 0
    for bkt in buckets:
        for e in bkt:
            s[i] = e
            i += 1
lst = [2, 3, 4, 8, 9, 12, 3, 2, 4, 12]
bucketSort(lst, 13)
print(lst) #>>[2, 2, 3, 3, 4, 4, 8, 9, 12, 12]
lst = [(-2, "Jack"), (8, "Mike"), (2, "Jane"), (2, "John")]
bucketSort(lst, 12, lambda x: x[0]+2)  # 取值范围写大一些也无妨
print(lst) #>>[(-2, 'Jack'), (2, 'Jane'), (2, 'John'), (8, 'Mike')]
lst = ["Jack", "Mike", "Lany", "Ada"]
bucketSort(lst, 26, lambda x: ord(x[0])-ord("A"))
print(lst) #>>['Ada', 'Jack', 'Lany', 'Mike']

