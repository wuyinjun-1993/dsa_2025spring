result = [0] * 4 	#等价于 result = [0,0,0,0]，存放摆放方案

#result[i]表示第i行的皇后已经放在result[i]这个位置

def isOk(n,pos):	#判断第n行的皇后放在位置pos是否可行

#此时第0行到第n-1行的皇后的摆放位置已经存放在result[0]至result[n-1]中
    for i in range(n):#检查位置pos是否会和前面0~n-1行已经摆好的皇后冲突
        if result[i] == pos or abs(i-n) == abs(result[i] - pos):
             return False
    return True

def main():
    for p0 in range(4):	#枚举第0行所有可能位置
          result[0] = p0	#第0行的皇后放在第p0列
          for p1 in range(4): 	#枚举第1行所有可能位置
                if isOk(1,p1):
                    result[1] = p1  #第1行的皇后放在第p1列
                    for p2 in range(4): #枚举第2行所有可能位置
                        if isOk(2,p2):
                            result[2] = p2
                            for p3 in range(4): #枚举第3行所有可能位置
                                if isOk(3,p3):
                                    result[3] = p3
                                    for x in result: #找到成功摆法，输出之
                                        print(x,end = " ")
                                    print("")
main()