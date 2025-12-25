def solution(arr, intervals):
    new_li = []
    for i in range(len(intervals)):
        a, b = intervals[i]
        
        new_li.extend(arr[a:b+1])
        
    return new_li