from dequeue1 import Deque
def palchecker(astring):
    chardeque = Deque()
    for ch in astring:
        chardeque.addRear(ch)
    stillEqual = True
    while chardeque.size()>1 and stillEqual:
        first = chardeque.removeFront()
        last = chardeque.removeRear()
        if first != last:
            stillEqual = False
    return stillEqual
print(palchecker("lsdkjfskf"))
print(palchecker("radar"))