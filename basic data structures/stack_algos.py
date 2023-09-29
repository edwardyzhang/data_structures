from stack import Stack, StackLinkedList

def moveToTop(s1, s2):
    #algorithm that moves the top value on one stack to the top of another stack
    top = s1.pop()
    s2.push(top)

def botToTop(s1):
    #algorithm that moves the bottom of the stack to the top and the moves the rest one down
    temp = Stack()
    
    while not s1.isEmpty():
        val = s1.pop()
        temp.push(val)

    bot = temp.pop()

    while not temp.isEmpty():
        val = temp.pop()
        s1.push(val)
        
    s1.push(bot)

def infixToPostfix(s):
    #taking a string of an expression in infix notation, return the expression in postfix notation
    oper = ['+', '-', '*', '/', '(', ')'] 
    operators = Stack()
    operands = Stack()

    postfix = ""

    for i in s:
        if i not in oper:
            operators.push(i)
        else:
            if not operands.isEmpty(): 
                if oper.index(i) < oper.index(operands.peek()):
                    postfix += operators.pop()
                    postfix += operators.pop()
                    postfix += operands.pop()
            operands.push(i)
    while not operators.isEmpty():
        postfix += operators.pop()
    while not operands.isEmpty():
        postfix += operands.pop()    
    
    return postfix

print (infixToPostfix('5*7+6*(8+2)*3'))