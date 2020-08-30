# 1 Modify the infix-to-postfix algorithm so that it can handle errors.


from pythonds.basic import Stack

def infixToPostfix(infixexpr):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opStack = Stack()
    postfixList = []
    #tokenList = infixexpr.split()
    tokenList = [char for char in infixexpr] # DA_20_20 mod
    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        elif token != " ": # not affected by spaces now. # DA 20_20 mod
            while (not opStack.isEmpty()) and \
               (prec[opStack.peek()] >= prec[token]):
                  postfixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    return " ".join(postfixList)

print(infixToPostfix("A * B + C * D"))
print(infixToPostfix("( ( A + B) * C - ( D - E ) ) * ( F + G )")) #unbalanced parenthesis just gets pushed onto end now with no error

# 2 Modify the postfix evaluation algorithm so that it can handle errors.
def postfixEval(postfixExpr):
    operandStack = Stack()
    tokenList = [char for char in postfixExpr] # DA_20_20 mod

    for token in tokenList:
        if token in "0123456789":
            operandStack.push(int(token))
        elif token in "*/+-" and operandStack.size() > 1:# DA_20_20 handle errors mod
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            result = doMath(token,operand1,operand2)
            operandStack.push(result)
    return operandStack.pop()

def doMath(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    elif op=="-":
        return op1 - op2

print(postfixEval('7 8 + 32 - +'))

#modifications allow uneven spaces in input expressions and not popping 2 operands from stack of size 1 or less

#3 Implement a direct infix evaluator that combines the functionality of infix-to-postfix conversion
# the postfix evaluation algorithm. Your evaluator should process infix tokens from left to right 
# and use two stacks, one for operators and one for operands, to perform the evaluation.

print(postfixEval(infixToPostfix("1 * 2 + 3 * 4")))

#4 Turn your direct infix evaluator from the previous problem into a calculator.
# same as above basically
