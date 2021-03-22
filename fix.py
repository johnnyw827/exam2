#empty list for output
ls = [] 
#store operators in stack
stack = ()
infix_p = 'A + B * C / D'
#Operators and please excuse my dear aunt sally.
operator = {}
operator['+'] = 1
operator['-'] = 1
operator['*'] = 2
operator['/'] = 2
operator['^'] = 3

def check_empty(stack):
    return stack.items == []

#Look at each element.
for op in infix_p:
    if op == ' ':
        continue
    #Check for operators and store in stack
    if op not in operator.keys():
        ls.append(op)
    if op in operator.keys() and stack.is_empty():
        
