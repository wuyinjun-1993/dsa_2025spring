MX = 110
INF = 1 << 30
class Road:
    def __init__(self,d,L,t):
       self.d,self.L,self.t = d,L,t

#邻接表。cityMap[i]是从点i有路连到的城市集合
cityMap = [[] for i in range(MX)] 
minLen = INF  #当前找到的最优路径的长度
totalLen = 0   #正在走的路径的长度
totalCost = 0 #正在走的路径的花销
visited = [0] * MX  #城市是否已经走过的标记
minL = [[INF for j in range(10100)] for i in range(MX)]
#minL[i][j]表示从1到i点的，花销为j的最短路的长度


def Dfs(s): #从 s开始向N行走
    global N,minLen,totalLen,totalCost,cityMap,K
    if s == N :
        minLen = min(minLen,totalLen)
        return
    for i in range( len(cityMap[s])):
        d =  cityMap[s][i].d  #s 有路连到d
        if  visited[d] == 0:
            cost = totalCost +  cityMap[s][i].t
            if cost > K:
                continue
            if totalLen+cityMap[s][i].L >= minLen or \
                 totalLen + cityMap[s][i].L >= minL[d][cost]:
                continue
            totalLen += cityMap[s][i].L
            totalCost +=  cityMap[s][i].t
            minL[d][cost] = totalLen
            visited[d] = 1
            Dfs(d)
            
            
            visited[d] = 0
            totalCost -=  cityMap[s][i].t
            totalLen -= cityMap[s][i].L

#main
K  = int(input())
N = int(input())
R = int(input())
for i in range(R):
    r = Road(0,0,0)
    s,r.d,r.L,r.t = map(int,input().split())
    if s != r.d:
        cityMap[s].append(r)
totalLen = totalCost = 0
visited[1] = 1
Dfs(1)
if minLen < INF:
    print(minLen)
else:
    print(-1)

