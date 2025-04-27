
MAX = 30000
parent = [ 0 for i in range(MAX+10) ]
total = [ 0 for i in range(MAX+10) ] 
#total[GetRoot(a)]是a所在的group的人数
def GetRoot( a ):  #获取a的根,并把a的父结点改为根
	if parent[a]!= a:
		parent[a] = GetRoot(parent[a])
	return parent[a]
def Merge( a, b ):
	p1 = GetRoot(a)
	p2 = GetRoot(b)
	if p1 == p2:
		return
	total[p1] += total[p2]
	parent[p2] = p1



while True:
	n, m = list( map( int, input().split() ) )
	if n == 0 and m == 0:	
		break
	for i in range(n):
		parent[i] = i
		total[i] = 1
	for i in range(m):
		lst = list( map( int, input().split() ) )
		k = lst[0]
		h = lst[1]
		for j in range( 2, k + 1 ):
			Merge( h, lst[j] )
	print( total[GetRoot(0)] ) 
