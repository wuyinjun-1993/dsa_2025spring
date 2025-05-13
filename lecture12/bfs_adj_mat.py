from queue import Queue

def bfs_adj_mat(graph, start):
    start.setDistance(0)
    start.setPred(None)
    vertQueue = Queue()
    vertQueue.enqueue(start)  # Store vertex indices, not objects
    
    while(vertQueue.size()>0):
        currentVert = vertQueue.dequeue()
        for neighbor_idx in graph.get_neighbors(currentVert.get_id()):
            nbr = graph.getVertex(neighbor_idx)
            if nbr.getColor() == 'white':
                nbr.setColor('gray')
                nbr.setDistance(currentVert.getDistance()+1)
                nbr.setPred(currentVert)
                vertQueue.engueue(nbr)
        
        currentVert.setColor('black')
        

def traverse(y):
    x=y
    while(x.getPred()):
        print(x.getId())
        x= x.getPred()
    print(x.getId())
    
    