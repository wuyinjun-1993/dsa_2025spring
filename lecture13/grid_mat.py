visited = [ [ 0 for i in range(50) ] for i in range(30) ]
def ways( i, j, n):
	if n == 0:
		return 1
	visited[i][j] = 1
	num = 0
	if not visited[i][j-1]:
		num+= ways(i,j-1,n-1)
	if not visited[i][j+1]:
		num+= ways(i,j+1,n-1)
	if not visited[i+1][j]:
		num+= ways(i+1,j,n-1)
	visited[i][j] = 0
	return num

n = int( input() )
print( ways(0,25,n) )
