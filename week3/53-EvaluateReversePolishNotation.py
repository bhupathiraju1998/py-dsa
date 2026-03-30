tokens = [2,3,"*",1,"-"]
operators = ["*","+","-","/"]
stack = []
for token in tokens:
    if token not in operators:
        stack.append(int(token))
    else:
        b = stack.pop()
        a = stack.pop()
        
        if token == '+': stack.append(a + b)
        elif token == '-': stack.append(a - b)
        elif token == '*': stack.append(a * b)
        elif token == '/': stack.append(int(a / b)) #int will round to zero 

print(stack)