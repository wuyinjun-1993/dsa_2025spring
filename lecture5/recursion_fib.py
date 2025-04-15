
def fib(n):
    if n==1 or n==2:
        return 1
    else:
        t= fib(n-1)
        return t+ fib(n-2)

print(fib(4))



def fib(n):
    class Status:  #放入栈中的元素
        def __init__(self,n,t,r):
            self.n,self.t,self.r = n,t,r
    stack = [Status(n,None,'c')]
    retVal = retAdr = None  #retVal是返回值，retAdr是返回地址
    while stack != []:
        status = stack[-1]
        n = status.n
        if n == 2 or n == 1:
            retVal = 1
            retAdr = status.r
            stack.pop()
        else: 
            if retAdr == None: 
                stack.append(Status(n-1, None, 'a')) 
            elif retAdr == 'a':
                stack[-1].t = retVal
                stack.append(Status(n-2,None,'b'))
                retAdr = None
            elif retAdr == 'b':
                retVal = status.t + retVal
                retAdr = status.r
                stack.pop()
            else:
                stack.pop()
    return retVal

