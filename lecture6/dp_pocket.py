
N = int( input() )
Ways = [ [ 0 for i in range(50) ] for i in range(50) ] 
# Ways[i][j]表示从前j种物品里凑出体积i的方法数
a = [ 0 ]
for i in range( 1, N+1 ):
    a.append( int(input()) )
    Ways[0][i] = 1
Ways[0][0] = 1
for w in range( 1, 41 ):
    for k in range( 1, N+1 ):
        Ways[w][k] = Ways[w][k-1]
        if w-a[k] >= 0:
            Ways[w][k] += Ways[w-a[k]][k-1]
print( Ways[40][N] )

