def solution(arr):
    b = []
    for i in arr:
        for _ in range(i):
            b.append(i)
    return b