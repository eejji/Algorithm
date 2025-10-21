def stack_(sen):
    stack = []    

    for ch in sen:
        if ch == "(":
            stack.append("(")
        elif ch == ")":
            if len(stack) == 0:
                return 'no'
            elif stack.pop() == "(":
                pass
            else:
                return 'no'
        elif ch == "[":
            stack.append("[")
        elif ch == "]":
            if len(stack) == 0:
                return 'no'
            elif stack.pop() == "[":
                pass
            else:
                return 'no'

    if len(stack) == 0:
        return 'yes'
    else: return 'no'
            
while True:
    
    sen = input()
    
    if sen == '.':
        break
        
    else:
        answer = stack_(sen)
        print(answer)