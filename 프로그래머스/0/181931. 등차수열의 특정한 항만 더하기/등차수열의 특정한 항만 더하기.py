def solution(a, d, included):
    
    results = 0
    
    for i in range(len(included)):
        
        if included[i]:
            results+= a
            a += d
        else:
            a += d
            continue
              
    return results