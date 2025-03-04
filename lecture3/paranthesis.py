class Stack:
    def __init__(self):
        self.items =[]
    def isEmpty(self):
        return self.items ==[]
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)
    
def parChecker(symbolstring):
    s=Stack()
    balanced = True
    index=0
    while index< len(symbolstring) and balanced:
        symbol = symbolstring[index]
        if symbol =="(":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced= False
            else:s.pop()
        index=index+1
    if balanced and s.isEmpty():
        return True
    else:
        return False

print(parChecker("((()))"))
print(parChecker('(()'))