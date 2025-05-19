class Edge:
	def __init__(self,v,w):
		self.v,self.w = v,w  #v是顶点，w是权值
def topoSort(G): #G是邻接表，顶点从0开始编号
    #G[i][j]是Edge对象
    n = len(G)
    import queue
    inDegree = [0] * n #inDegree[i]是顶点i的入度
    q = queue.Queue()
    for i in range(n):
        for e in G[i]:
            inDegree[e.v] += 1
    for i in range(n):
        if inDegree[i] == 0:
            q.put(i)
    seq = []
    while not q.empty():
        k = q.get()
        seq.append(k)
        for e in G[k]:
            inDegree[e.v] -= 1  #删除边(k,v)后将v入度减1
            if inDegree[e.v] == 0:
                q.put(e.v)
    if len(seq) != n:  #如果拓扑序列长度少于点数，则说明有环
        return None
    else:
        return seq
