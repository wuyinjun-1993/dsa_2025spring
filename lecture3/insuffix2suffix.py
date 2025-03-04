from stack import Stack

def infixToPostfix(infixexpr):
    prec={}
    prec["*"]=3
    prec["/"]=3
    prec["+"]=2
    prec["-"]=2
    prec["("]=1
    opstack = Stack()
    postfixList =[]
    tokenList =infixexpr.split()

    for token in tokenList:
        if token in "ABCDEFGHIIKLMNOPORSTUVWXYz" or token in "0123456789":
            postfixList.append(token)
        elif token == '(':
            opstack.push(token)
        elif token ==')':
            topToken = opstack.pop()
            while topToken !='(':
                postfixList.append(topToken)
                topToken = opstack.pop()
        else:
            while(not opstack.isEmpty()) and \
                (prec[opstack.peek()]>= prec[token]):
                postfixList.append(opstack.pop())
            opstack.push(token)
    
    while not opstack.isEmpty():
        postfixList.append(opstack.pop())
    return " ".join(postfixList)
