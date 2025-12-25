def solution(num_list):
    for i, idx in enumerate(num_list):
        if idx < 0:
            return i
    return -1
        
    