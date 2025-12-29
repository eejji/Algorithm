def solution(arr, queries):
    for s, e in queries:
        arr[s:e+1] = [x + 1 for x in arr[s:e+1]]

    return arr