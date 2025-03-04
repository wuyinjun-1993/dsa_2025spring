k1=1
k2=2
def f():
    n1 = 10
    n2 = 20
    def g():
        print("k1 =",k1,"n1 =",n1)
        nonlocal n1
        global k1
        
        k1 *= 10
        n1 *= 10
        print("k2 =",k2,"n2 =",n2)

    g()

    print("k1 =",k1,"n1 =",n1)
f()