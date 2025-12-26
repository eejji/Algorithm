def solution(num_list, n):
    a = num_list[n:] + num_list[:n]
    
    return a