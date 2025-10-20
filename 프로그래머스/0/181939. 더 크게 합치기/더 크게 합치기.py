def solution(a, b):
    n1 = int(str(a) + str(b))
    n2 = int(str(b) + str(a))
    
    if n1 > n2:
        return n1
    else:
        return n2