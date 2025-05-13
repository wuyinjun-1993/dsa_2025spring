
class Vertex_adj_mat:
    def __init__(self,key):
        self.id = key
        self.color = 'white'  # Initial color for BFS/DFS
        self.distance = float('inf')  # Initial distance
        self.pred = None  # Predecessor vertex
        
    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr]= weight

    def getId(self):
        return self.id

    def getWeight(self,nbr):
        return self.connectedTo[nbr]
    
    def getPred(self):
        return self.pred

    def setPred(self, pred):
        self.pred = pred

    def getColor(self):
        return self.color

    def setColor(self, color):
        self.color = color

    def getDistance(self):
        return self.distance

    def setDistance(self, distance):
        self.distance = distance
    
class Graph_adj_mat:
    def __init__(self,num_vertices=8):
        self.vertList ={}
        self.adj_matrix = [[0] * num_vertices for _ in range(num_vertices)]
        self.numVertices=num_vertices
    
    def addVertex(self,key):
        self.numVertices = self.numVertices +1
        newVertex =Vertex_adj_mat(key)
        self.vertList[key]= newVertex
        return newVertex

    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None
    
    def __contains__(self,n):
        return n in self.vertList
    
    def addEdge(self, v1, v2, weight=1):
        if 0 <= v1 < self.num_vertices and 0 <= v2 < self.num_vertices:
            self.adj_matrix[v1][v2] = weight
            self.adj_matrix[v2][v1] = weight  # For undirected graph (remove if directed)

    def get_neighbors(self, idx):
        neighbors = []
        for j in range(self.num_vertices):
            if self.adj_matrix[idx][j] != 0:
                neighbors.append(j)
        return neighbors

    def getVertices(self):
        return self.vertList.keys()
    
    def __iter__(self):
        return iter(self.vertList.values())


g= Graph_adj_mat()
for i in range(6):
    g.addVertex(i)


    
print(g.vertList[0])


g.addEdge(0,1,5)
g.addEdge(0,5,2)
g.addEdge(1,2,4)
g.addEdge(2,3,9)
g.addEdge(3,4,7)
g.addEdge(3,5,3)
g.addEdge(4,0,1)
g.addEdge(5,4,8)
g.addEdge(5,2,1)
        


