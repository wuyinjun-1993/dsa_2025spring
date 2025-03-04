from stack import Stack
def postfixEval(postfixExpr):
    operandstack =Stack()
    tokenList = postfixExpr.split()
    for token in tokenList:
        if token in "0123456789":
            operandstack.push(int(token))
        else:
            operand2 = operandstack.pop()
            operand1 = operandstack.pop()
            result = doMath(token,operand1,operand2)
            operandstack.push(result)
    return operandstack.pop()

def doMath(op,op1, op2):
    if op =="*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op =="+":
        return op1 + op2
    else:
        return op1 - op2
    