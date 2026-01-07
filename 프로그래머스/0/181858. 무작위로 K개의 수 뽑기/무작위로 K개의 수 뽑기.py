def solution(arr, k):
    result = []
    for i in range(len(arr)):
        if arr[i] in result:
            pass
        else:
            result.append(arr[i])

    if len(result) < k:
        n = k-len(result)
        for _ in range(n):
            result.append(-1)
    else:
        result = result[:k]
    return result