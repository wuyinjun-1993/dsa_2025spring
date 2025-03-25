
fib_res=[-1]*100

def fib(n):
    if n==1 or n==2:
        return 1
    elif fib_res[n] >= 0:
        return fib_res[n]
    else:
        fib_res[n-1]= fib(n-1)
        fib_res[n-2]= fib(n-2)
        return fib_res[n-1]+ fib_res[n-2]

print(fib(4))