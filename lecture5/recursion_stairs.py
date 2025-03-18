def stairs( n ):
    if n < 0:
        return 0
    if n == 0:
        return 1
    return stairs( n-1 ) + stairs( n-2 )
try:
    while True:
        N = int(input())
        print( stairs( N ))
except EOFError:
    pass





def stairs( n ):
    if n < 2:
        return 1
    a1,a2 = 1,1
    for i in range(2,n+1):
        a3 = a1 + a2
        a1,a2 = a2,a3
    return a3
try:
    while True:
        N = int(input())
        print( stairs( N ))
except EOFError:
    pass