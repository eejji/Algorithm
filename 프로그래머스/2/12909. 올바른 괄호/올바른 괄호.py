def solution(s):
    
    stacks = []
    
    for i in s:
        if i == "(":
            stacks.append("(")
        else:
            if not stacks:
                return False
            stacks.pop()
            

    return len(stacks) == 0