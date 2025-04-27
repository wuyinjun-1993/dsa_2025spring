
def GetRoot(a):
    if parent[a] == a:
        return a
    return GetRoot(parent[a])


def GetRoot(a):
	if parent[a] != a:
		parent[a] = GetRoot(parent[a])
	return parent[a]


N=10

parent = [i for i in range(N)]
def Merge(a,b):
 #把b树根挂到a树根下
	parent[GetRoot(b)] = GetRoot(a)

def Query(a,b):
  #查询a,b是否位于同一棵树
	return GetRoot(a) == GetRoot(b)

