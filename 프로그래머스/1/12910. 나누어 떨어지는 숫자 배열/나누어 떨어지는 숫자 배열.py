def solution(arr, divisor):
    new = sorted([arr[i] for i in range(len(arr)) if arr[i] % divisor==0])
    if len(new) > 0:
        return new
    else: return [-1]