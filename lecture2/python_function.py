def square(x):
    return x*x
def inc(x):
    return x+1
def combine(f,g,x):
    return f(g(x))
print(combine(square,inc,4))#>>25
print(combine(inc,square,4))#>>17