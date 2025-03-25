n = int(input())
vlist=[1,1,2,4,8]

def total(n):
    if n <= 4:
        return vlist[n]
    else:
        return total(n-1)+total(n-2)+ total(n-3)+ total(n-4)


print(total(n))




n = int(input())
cache ={0:1,1:1,2:2,3:4,4:8}

def total(n):
    if n <= 4:
        return cache[n]
    elif n in cache:
        return cache[n]
    else:
        print("cache not hit::", n)
        cache[n]=total(n-1)+ total(n-2)\
            + total(n-3)+ total(n-4)
    return cache[n]



n = int(input())
cache ={0:1,1:1,2:2,3:4,4:8}

def total(n):
    if n<= 4:
        return cache[n]
    else:
        for i in range(5,n + 1):
            cache[i]=cache[i-1]+cache[i-2]\
                + cache[i-3] + cache[i-4]
    return cache[n]

print(total(n))


