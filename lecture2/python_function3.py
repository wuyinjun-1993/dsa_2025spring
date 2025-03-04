def func (x):
    def g(y) :
        nonlocal x
        x+= 1
        return x+y
    return g
f= func(10)
print(f(4))
print(f(5))
g= func(20)
print(g(4))
print(g(5))