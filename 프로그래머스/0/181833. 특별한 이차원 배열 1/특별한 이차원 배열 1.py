def solution(n):
    new = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                new[i][j] = 1
    return new