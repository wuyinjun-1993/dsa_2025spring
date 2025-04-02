
def tailRecursiveQuickSort(a,s,e):
	while s < e:
		i,j = s,e
		while i != j: #分两半的操作
			while i < j and a[i] <= a[j]:
				j -= 1
			a[i],a[j] = a[j],a[i]
			while i < j and a[i] <= a[j]:
				i += 1
			a[i], a[j] = a[j], a[i]
		if i-s < e - i: #每次选短的那一半进行递归快排，递归层数就不会超过log(n)
			tailRecursiveQuickSort(a,s,i-1)
			s = i + 1
		else:
			tailRecursiveQuickSort(a,i+1,e)
			e = i - 1


