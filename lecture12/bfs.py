from queue import Queue

def bfs(g,start):
    start.setDistance(0)
    start.setPred(None)
    vertQueue = Queue()
    vertQueue.enqueue(start)
    while(vertQueue.size()>0):
        currentVert = vertQueue.dequeue()
        for nbr in currentVert.getConnections():
            if(nbr.getColor()=='white'):
                nbr.setColor('gray')
                nbr.setDistance(currentVert.getDistance()+1)
                nbr.setPred(currentVert)
                vertQueue.engueue(nbr)
        currentVert.setColor('black')
            

def bft(g):
    for aVertex in g.getVertices():
        if aVertex.getColor()=='white':
            bfs(g,aVertex)

def traverse(y):
    x=y
    while(x.getPred()):
        print(x.getId())
        x= x.getPred()
    print(x.getId())
    
    