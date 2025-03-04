from math import sqrt
n= int(input("please input number:"))
for i in range(2, int(sqrt(n))+1):
    if n%i==0:
        print(f"{n} is NoT a prime number.")
        break
else:
    print(f"{n} is a prime number.")
