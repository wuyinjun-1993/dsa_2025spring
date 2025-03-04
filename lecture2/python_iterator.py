a=[1,2,3]
for i in a:
    print(i)
    
print("Iteration new:")
it=iter(a)
while True:
    try:
        i=next(it)
        print(i)
    except StopIteration:
        break