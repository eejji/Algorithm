def solution(arr, queries):
    
    for i in range(len(queries)):
        a = queries[i][0]
        b = queries[i][1]
        
        c = arr[a]
        d = arr[b]
        
        arr[a] = d
        arr[b] = c
        
    
    return arr