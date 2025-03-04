def square(x):
    return x * x

def inc(x):
    return x+ 1

def combineFunctions(f,g):
    return lambda x:f(g(x)) 
def powerFunction(f,n):
    def h(x):
        for i in range(n):
            x= f(x)
        return x
    return h

print(combineFunctions(square,inc)(4))
print(powerFunction(inc,5)(1))
print(powerFunction(square,4)(2))