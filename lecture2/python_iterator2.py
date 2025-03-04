class MyRange:

    def __init__(self,n):
        self.idx= 0
        self.n= n

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.idx < self.n:
            val= self.idx
            self.idx += 1
            return val
        else:
            raise StopIteration()

for i in MyRange(5):
    print(i,end=",")
    print([i for i in MyRange(5)])
    
x=MyRange(4)
for i in x:
    print(i,end=",")

for i in x:
    print(i,end=",")