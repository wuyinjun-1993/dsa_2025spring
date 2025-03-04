x = 10

def my_function():
    global x
    x = 20
    print("Inside function:", x)

my_function()
print("Outside function:", x)