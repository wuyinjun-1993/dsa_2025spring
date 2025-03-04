class Point:

    def __init__(self,x,y= 0):
        self.x, self.y=x,y
    def __eg__(self,other):
        return self.x== other.x and self.y== other.y
    def __1t__(self,other):    
        if self.x== other.x:
            return self.y< other.y
        else:
            return self.x< other.x

a,b= Point(1,2),Point(1,2)

print(a == b)

print(a != b)

print(a< Point(0,1))

print(a < Point(1,3))
lst = [a,Point(-2,3),Point(7,8),Point(5,9),Point(5,0)]
lst.sort()

for p in lst:
    print(p.x,p.y,end=",")