class A:
    def __init__(self,x):
        self.x = x

a,b = A(5),A(5)	#两个A(5)不是同一个，因此a和b的id不同
dt = {a:20,A(5):30,b:40}	#三个元素的键id不同，因此在不同槽里
print(len(dt),dt[a],dt[b])     #>>3 20 40
# print(dt[A(5)])     	#runtime error


