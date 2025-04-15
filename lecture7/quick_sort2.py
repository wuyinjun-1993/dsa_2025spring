
def partition(alist,first,last):
    pivotvalue = alist[first]

    leftmark= first+1
    rightmark=last

    done = False
    while not done:
        while leftmark <= rightmark and alist[leftmark]<= pivotvalue:
            leftmark=leftmark +1
        while alist[rightmark]>= pivotvalue and rightmark >= leftmark:
            rightmark=rightmark -1
        if rightmark< leftmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark]= alist[rightmark]
            alist[rightmark]= temp
        
    temp = alist[first]
    alist[first]= alist[rightmark]
    alist[rightmark]= temp

    return rightmark


# def tailRecursiveQuickSort(a,s,e):
# 	while s < e:
# 		i,j = s,e
# 		splitpoint = partition(a,s,e)
# 		while i != j: #分两半的操作
# 			while i < j and a[i] <= a[j]:
# 				j -= 1
# 			a[i],a[j] = a[j],a[i]
# 			while i < j and a[i] <= a[j]:
# 				i += 1
# 			a[i], a[j] = a[j], a[i]
# 		if i-s < e - i: #每次选短的那一半进行递归快排，递归层数就不会超过log(n)
# 			tailRecursiveQuickSort(a,s,i-1)
# 			s = i + 1
# 		else:
# 			tailRecursiveQuickSort(a,i+1,e)
# 			e = i - 1



def tailRecursiveQuickSort(a,s,e):
	while s < e:
		splitpoint = partition(a,s,e)
  
		if splitpoint-s < e - splitpoint: 
			#每次选短的那一半进行递归快排，递归层数就不会超过log(n)
			tailRecursiveQuickSort(a,s,splitpoint-1)
			s = splitpoint + 1
		else:
			tailRecursiveQuickSort(a,splitpoint+1,e)
			e = splitpoint - 1

