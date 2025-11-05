def solution(arr, queries):
    answer = []
    
    for i in range(len(queries)):
        mid = []
        a = queries[i][0]
        b = queries[i][1]
        c = queries[i][2]
        
        for j in range(a, b+1):
            if arr[j] > c:
                mid.append(arr[j])
        try:
            answer.append(min(mid))
        except:
            answer.append(-1)
    
    return answer