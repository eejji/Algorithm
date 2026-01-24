def solution(arr):
    if len(arr) == 1:
        return [-1]

    else:
        del arr[arr.index(min(arr))]
        return arr