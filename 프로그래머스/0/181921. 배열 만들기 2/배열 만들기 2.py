def valid(x):
    s = str(x)
    
    for ch in s:
        if ch not in {'0', '5'}:
            return False
    return True

def solution(l, r):
    
    answer = []
    for i in range(l, r+1):
        if valid(i):
            answer.append(i)
        else:
            pass
        
        
    if len(answer) == 0:
        answer.append(-1)
        return answer
    else:
        return answer