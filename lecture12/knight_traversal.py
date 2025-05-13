from graph import Graph

def genLegalMoves(x,y,bdsize):
    newMoves =[]
    moveOffsets =[(-1,-2),(-1,2),(-2,1),(-2,1)
                  ,(1,-2),(1,2),(2,-1),(2,1)]
    for i in moveOffsets:
        newX=x+ i[0]
        newY=y+ i[1]
        if legalCoord(newX,bdsize) and legalCoord(newY,bdsize):
            newMoves.append((newX,newY))
    return newMoves

def legalCoord(x,bdsize):
    if x>= 0 and x< bdsize:
        return True
    else:
        return False
    
    
def knightGraph(bdsize):
    ktGraph = Graph()
    for row in range(bdsize):
        for col in range(bdsize):
            nodeId = posToNodeId(row,col,bdsize)
            newPositions = genLegalMoves(row,col,bdsize)
            for e in newPositions:
                nid = posToNodeId(e[0],e[1],bdsize)
                ktGraph.addEdge(nodeId,nid)
    return ktGraph

def posToNodeId(row,col,bdsize):
    return row*bdsize+col


def knightTour(n,path,u,limit):
    u.setColor('gray')
    path.append(u)
    if n < limit:
        nbrList = list(u.getConnections())
        i=0
        done = False
        while i<len(nbrList) and not done:
            if nbrList[i].getColor()=='white':
                done = knightTour(n+1, path,nbrList[i],limit)
            i=i+1
        if not done: # prepare to backtrack
            path.pop()
            u.setColor('white')
    else:
        done = True
    return done

def orderByAvail(n):
    resList =[]
    for v in n.getConnections():
        if v.getColor()=='white':
            c=0
            for w in v.getConnections():
                if w.getColor()=='white':
                    c=c+1
            resList.append((c,v))
    resList.sort(key=lambda x:x[0])
    return [y[1] for y in resList]

