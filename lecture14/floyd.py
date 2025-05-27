

def floyd(G): #G是邻接矩阵，顶点编号从0开始算,无边则边权值为INF
    n = len(G)
    INF = 10**9
    prev = [[None for i in range(n)] for j in range(n)]
    #prev[i][j]表示到目前为止发现的从i到j的最短路上，j的前驱。
    dist = [[INF for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                dist[i][j] = 0
            else:
                if G[i][j] != INF: #i到j的边存在
                    dist[i][j] = G[i][j]
                    prev[i][j] = i
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    prev[i][j] = prev[k][j]
    return dist,prev
