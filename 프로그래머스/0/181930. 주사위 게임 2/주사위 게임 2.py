def solution(a, b, c):
    if len({a, b, c}) == 3:  
        return a + b + c
    
    elif a == b == c:  
        return (a + b + c) * (a**2 + b**2 + c**2) * (a**3 + b**3 + c**3)
    
    else:  
        return (a + b + c) * (a**2 + b**2 + c**2)