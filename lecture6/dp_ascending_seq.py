
N = int(input())
maxLen = [1 for i in range(N+10)]
a = list(map(int,input().split()))
for i in range(1,N):
#每次求以第i个数为终点的最长上升子序列的长度
    for j in range(0,i):
        #察看以第j个数为终点的最长上升子序列
        if a[i] > a[j]:
            maxLen[i] = max(maxLen[i],maxLen[j]+1)
print(max(maxLen))

#时间复杂度O(N2)


