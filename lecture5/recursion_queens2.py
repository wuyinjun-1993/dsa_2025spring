result = [0] * 12 	#等价于 result = [0,0,0,0]，存放摆放方案

#result[i]表示第i行的皇后已经放在result[i]这个位置

def isOk(n,pos):	#判断第n行的皇后放在位置pos是否可行

#此时第0行到第n-1行的皇后的摆放位置已经存放在result[0]至result[n-1]中
    for i in range(n):#检查位置pos是否会和前面0~n-1行已经摆好的皇后冲突
        if result[i] == pos or abs(i-n) == abs(result[i] - pos):
             return False
    return True

def queen(N,m):#解决N皇后问题，现在第0行到第m-1行的m个的皇后已经摆放好了
                  #要摆放第m行的皇后，
    if m == N: #已经摆好了N个皇后，说明问题已经解决，输出结果即可
        for k in range(N):
            print(result[k], end=" ")
        print("")
        return True
    succeed = False
    for i in range(N):    #枚举所有位置
        if isOk(m,i):      #看可否将第m行皇后摆在第i列
            result[m] = i  #可以摆在第i列，就摆上
            succeed = queen(N,m+1) or succeed   #接着去摆放第i+1行的皇后
    return succeed
N = int(input())
if not queen(N,0):
    print("NO ANSWER")
