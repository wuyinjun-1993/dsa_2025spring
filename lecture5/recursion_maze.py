class Maze:
    def __init__(self,mazeFileName):
        rowsInMaze=0
        self.columnsInMaze=0
        self.mazelist =[]
        mazeFile = open(mazeFileName,'r')
        rowsInMaze=0
        for line in mazeFile:
            rowList =[]
            col=0
            for ch in line[:-1]:
                rowList.append(ch)
                if ch =='S':
                    self.startRow = rowsInMaze
                    self.startCol=col
                col=col+1
            rowsInMaze=rowsInMaze+1
            self.mazelist.append(rowList)
            self.columnsInMaze=len(rowList)
            
