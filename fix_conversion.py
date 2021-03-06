class Stacks:
    def __init__(self):
        self.items = []

    def push(self,data):
        self.items.append(data)
    
    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def is_empty(self):
        return self.items == []
    
    def printStack(self):
        return self.items

# converts infix expression to postfix expression
def infix_to_postfix(st,priority,inf):
    pst = []
    for el in inf:
        if el == ' ':
            continue
        # print("checking: ",el)
        # opening parenthesis
        if el == '(':
            st.push(el)

        elif el == ')':
            while not st.is_empty():
                if st.peek() == '(':
                    st.pop()
                    break
                else:
                    pst.append(st.pop())
        # if it's an operand
        elif el not in priority.keys() and (el != '(' or el != ')'):
            # print("operand:",el)
            pst.append(el)

        # if it's an operator and stack is empty
        elif el in priority.keys() and  st.is_empty():
            # print("operator: ",el)
            st.push(el)
         # if it's an operator of higher priority than the priority of TOS element
        elif el in priority.keys() and not st.is_empty() and st.peek() =='(':
            # print("operator:",el)
            st.push(el)

        # if it's an operator of higher priority than the priority of TOS element
        elif el in priority.keys() and not st.is_empty() and priority[el] >= priority[st.peek()]:
            # print("operator: ",el)
            st.push(el)
        # if it's an operator of lower priority than the priority of TOS element
        elif el in priority.keys() and not st.is_empty() and priority[el] < priority[st.peek()]:
            # print("operator: ",el)
            while not st.is_empty():
                if st.peek() == '(':
                    break
                elif priority[st.peek()] >= priority[el]:
                    pst.append(st.pop())
                else:
                    break
            st.push(el)
        # print("stack: ",st.printStack())
        # print("postfix:",pst)
    while not st.is_empty():
        pst.append(st.pop())
    return pst

def reverse(exp):
    rev_exp = []
    for i in range(len(exp)-1,-1,-1):
        if exp[i] == '(':
            e = ')'
        elif exp[i] == ')':
            e = '('
        else:
            e = exp[i]
        rev_exp.append(e)
    return rev_exp

def infix_to_prefix(st,priority,inf):
    rev_exp = reverse(inf)
    pst = infix_to_postfix(st,priority,rev_exp)
    return reverse(pst)




if __name__=="__main__":
    priority = {}
    priority['+'] = 1
    priority['-'] = 1
    priority['*'] = 2
    priority['/'] = 2
    priority['^'] = 3
    
    st = Stacks()
    inf = input("Enter the infix expression:")
    #print("input: a+b*(c^d-e)^(f+g*h)-i")
    #inf = "a+b*(c^d-e)^(f+g*h)-i"
    op = int(input("Postfix(1) or Prefix(2) or both(3)? (1,2 or 3) "))
    while True:
        if op == 1:
            print("Postfix expression: ",infix_to_postfix(st,priority,inf))
            break
        elif op == 2:
            print("Prefix expression: ",infix_to_prefix(st,priority,inf))
            break
        elif op == 3:
            print("Postfix expression: ",infix_to_postfix(st,priority,inf))
            print("Prefix expression: ",infix_to_prefix(st,priority,inf))
            break
        else:
            op = int(input("Postfix(1) or Prefix(2) or both(3)? (enter 1,2 or 3): "))
