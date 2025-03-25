
n = int(input())
D = []
def MaxSum(i,j):
    if i == n-1:
        return D[i][j]
    x = MaxSum(i+1,j)
    y = MaxSum(i+1,j+1)
    return max(x,y) + D[i][j]
def main():
    for i in range(n):
        lst = list(map(int,input().split()))
        D.append(lst)
    print(MaxSum(0,0))
main()


n = int(input())
D = []
maxSum = [[-1 for j in range(i+1)] for i in range(n)]
def MaxSum(i,j):
    if i == n-1:
        return D[i][j]
    if maxSum[i][j] != -1:
        return maxSum[i][j]
    x = MaxSum(i+1,j)
    y = MaxSum(i+1,j+1)
    maxSum[i][j] = max(x,y) + D[i][j]
    return maxSum[i][j]
for i in range(n):
       lst = list(map(int,input().split()))
       D.append(lst)
print(MaxSum(0,0))





n = int(input())
D = []
maxSum = [[-1 for j in range(i+1)] for i in range(n)]
def main():
    for i in range(n):
        lst = list(map(int,input().split()))
        D.append(lst)
    for i in range(n):
        maxSum[n-1][i] = D[n-1][i]
    for i in range(n-2,-1,-1):
        for j in range(0,i+1):
            maxSum[i][j] = 	max(maxSum[i+1][j],maxSum[i+1][j+1]) + D[i][j]
    print(maxSum[0][0])

main()


n = int(input())
D = []
def main():
    for i in range(n):
        lst = list(map(int,input().split()))
        D.append(lst)
    maxSum = D[n-1]
    for i in range(n-2,-1,-1):
        for j in range(0,i+1):
            maxSum[j] = max(maxSum[j],maxSum[j+1]) + D[i][j]
    print(maxSum[0])

main()


