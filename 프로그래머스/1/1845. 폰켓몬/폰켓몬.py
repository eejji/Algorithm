def solution(nums):
    set_len = len(set(nums))
    N = len(nums)//2

    if N < set_len :
        answer = N
    else :
        answer = set_len

    return answer