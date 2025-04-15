

def maxInWindows(num, size):
    queue = []
    res = []
    n= len(num)
    if n == 0 or n< size or size ==0:
        return res
    for i in range(n):
        if len(queue) != 0 and i- size >= queue[0]:
            queue.pop(0)
        while queue and num[i]>= num[queue[-1]]:
            queue.pop()
            
        queue.append(i)
    
        if queue and i>=size-1:
            res.append(num[queue[0]])
        
    return res

