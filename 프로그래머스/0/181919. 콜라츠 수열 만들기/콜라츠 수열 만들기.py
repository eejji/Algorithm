def solution(n):
    li = []
    
    while True:
        
        if n % 2 == 0:
            li.append(int(n))
            n = n /2
        else:
            li.append(int(n))
            n = 3* n + 1
            
        if n == 1:
            li.append(int(n))
            break
            
    
    return li