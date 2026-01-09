def solution(arr, n):
    if len(arr) % 2 == 0:
        return [arr[i] + n if i % 2 != 0 else arr[i] for i in range(len(arr))]
    else:
        return [arr[i] + n if i % 2 == 0 else arr[i] for i in range(len(arr))]