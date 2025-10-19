def solution(str1, str2):
    
    c = [] 
    
    for i in range(len(str1)):
        c.append(str1[i])
        c.append(str2[i])

                   
    return ''.join(map(str, c))

