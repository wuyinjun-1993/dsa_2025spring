
class Edge:
    def __init__(self,s,e,w):
        self.s ,self.e,self.w = s,e,w  #起点，终点，权值
    def __lt__(self,other):
        return self.w < other.w

def GetRoot(a):
	if parent[a] == a:
		return a
	parent[a] = GetRoot(parent[a])
	return parent[a]
def Merge(a, b):
	p1 = GetRoot(a)
	p2 = GetRoot(b)
	if p1 == p2: 	
		return
	parent[p2] = p1
 
 
while True:  #main
    try:
        N = int(input())
        parent = [i for i in range(N)]
        edges = []
        for  i in range(N):
            lst = list(map(int,input().split()))
            for j in range(N):
                edges.append(Edge(i,j,lst[j]))
        edges.sort() #排序复杂度O(ElogE）
        done = totalLen = 0
        for edge in edges:
            if GetRoot(edge.s) != GetRoot(edge.e):
                Merge(edge.s,edge.e)
                done += 1
                totalLen += edge.w
            if done == N - 1:
                break
        print(totalLen)
    except:  
        break