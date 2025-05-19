import math
EPS = 1e-6
def isZero( x ):
    return math.fabs(x) <= EPS
def count24( a , n ): #用列表a里面的头n个元素算24，返回能否成功
    if n == 1:
        if isZero( a[0] - 24 ):
            return True
        else:
            return False
    b = [ float() for i in range(5) ]
    for i in range( n-1 ):
        for j in range( i+1 , n ): #选 a[i]和a[j]算一下
            m = 0
            for k in range(n): #把a[i],a[j]以外的数放到b开头
                if k != i and k != j:
                    b[m] = a[k]
                    m = m+1
                    
            b[m] = a[i] + a[j]
            if count24(b , m+1): 
                return True
            b[m] = a[i] - a[j]
            if count24(b, m + 1):
                return True
            b[m] = a[j] - a[i]
            if count24(b, m + 1):
                return True
            b[m] = a[i] * a[j]
            if count24(b, m + 1):
                return True
            if not isZero(a[j]):
                b[m] = a[i] / a[j]
                if (count24(b, m+1)): return True
            if not isZero(a[i]):
                b[m] = a[j] / a[i]
                if (count24(b, m + 1)):
                    return True
    return False


#main
while True:
    a = input().split()
    a = [ int(c) for c in a ]
    if isZero( a[0] ):
        break
    if count24( a , 4 ):
        print( "YES" )
    else:
        print( "NO" )
