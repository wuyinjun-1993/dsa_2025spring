import timeit
import random

i = 10000
t = timeit.Timer("random.randrange(%d) in x" % i, "from __main__ import x, random")
x = list(range(i))  # Define `x` before using it in the Timer

lst_time = t.timeit(number=1000)
print("Time taken:", lst_time)