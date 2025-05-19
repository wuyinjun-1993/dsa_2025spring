import math
minArea = 1 << 30 #最优表面积
area = 0  #正在搭建中的蛋糕的表面积
minV = [0]*30 # minV[n]表示n层蛋糕最少的体积
minA = [0]*30 # minA[n]表示n层蛋糕的最少侧表面积
def MaxVforNRH(n,r,h):
#求在n层蛋糕，底层最大半径r，最高高度h的情况下，能凑出来的最大体积
    v = 0
    for i in range(n):
        v += (r - i ) *(r-i) * (h-i)
    return v
def Dfs(v, n, r, h):
#要用n层去凑体积v,最底层半径不能超过r,高度不能超过h
#求出最小表面积放入 minArea
    global minArea,area,M
    if n == 0:
        if v != 0: return
        else:
            minArea = min(minArea,area)
            return

    if v <= 0:
        return
    if minV[n] > v: #剪枝3
        return
    if area + minA[n] >= minArea: #剪枝1
        return
    if h < n or r < n: #剪枝2
        return

    if MaxVforNRH(n,r,h) < v: #剪枝4
    #这个剪枝最强！
        return
    #for rr in range(n,r+1): 这种写法比从大到小慢5倍
    for rr in range(r,n-1,-1):
        if n == M : #底面积
            area = rr * rr
        for hh in range(h,n-1,-1):
            area += 2 * rr * hh
            Dfs(v-rr*rr*hh,n-1,rr-1,hh-1)
            area -= 2 * rr * hh

#main
N = int(input())
M = int(input())  #M层蛋糕，体积N
minV[0] = minA[0] = 0
for  i in range(1,M+1):
    minV[i] = minV[i-1] + i * i * i
    minA[i] =  minA[i-1] + 2 * i * i
if  minV[M] > N:
    print(0)
else:
    maxH = int((N - minV[M-1])/(M*M)) + 1 #底层最大高度
    #最底层体积不超过 (N-minV[M-1]),且半径至少M
    maxR = int(math.sqrt((N-minV[M-1])/M)) + 1 #底层高度至少M
    area = 0
    minArea = 1 << 30
    Dfs( N,M,maxR,maxH)
    if  minArea == 1 << 30:
        print(0)
    else:
        print(minArea)
