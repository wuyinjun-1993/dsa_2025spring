
from pythonds.graphs import Graph

class DFsGraph(Graph):
    def __init__(self):
        super().__init__()
        self.time =0
        
    def dfs(self):
        for aVertex in self:
            aVertex.setColor('white')
            aVertex.setPred(-1)
        for aVertex in self:
            if aVertex.getColor()=='white':
                self.dfsvisit(aVertex)
                
    def dfsvisit(self,startVertex):
        startVertex.setColor('gray')
        
        self.time += 1
        startVertex.setDiscovery(self.time)
        for nextVertex in startVertex.getConnections():
            if nextVertex.getColor()=='white':
                nextVertex.setPred(startVertex)
                self.dfsvisit(nextVertex)
        startVertex.setColor('black')
        print(startVertex.getId())
        self.time += 1
        startVertex.setFinish(self.time)
        
    def dfs_norecursion(self):       
        for x in self:
            if x.getColor() == 'white':
                stack = [[x, 0]]  # 0表示只看了0个邻点
                x.setColor('gray')  # 标记为灰色（已发现但未处理完）
                while len(stack) > 0:
                    nd = stack[-1]  # nd[1]表示已经看过nd[1]个邻点
                    v = nd[0]
                    
                    if nd[1] == len(v.getConnections()):  # 所有邻点已处理完
                        v.setColor('black')  # 标记为黑色（已处理完）
                        stack.pop()
                    else:
                        for i in range(nd[1], len(v.getConnections())):
                            u = list(v.getConnections())[i]
                            nd[1] += 1  # 看过的邻点多了一个
                            if u.getColor() == 'white':  # 只有白色节点需要处理
                                stack.append([u, 0])
                                u.setPred(v) # 设置前驱
                                u.setColor('gray')  # 标记为灰色
                                break

def main():
    g = DFsGraph()
    for i in range(6):
        g.addVertex(i)
        
    g.addEdge(0, 1, 5)
    g.addEdge(0, 2, 3)
    g.addEdge(1, 3, 2)
    g.addEdge(1, 4, 4)
    g.addEdge(2, 4, 6)
    g.addEdge(3, 5, 7)
    
    print("DFS Traversal:")
    g.dfs()
    # g.dfs_norecursion()
    
main()