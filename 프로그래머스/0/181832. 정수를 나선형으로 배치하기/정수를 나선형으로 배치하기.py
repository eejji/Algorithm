def solution(n):
    answer = [[0]*n for _ in range(n)]

    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    r, c = 0, 0
    dist = 0

    for num in range(1, n*n+1):
        answer[r][c] = num

        next_r = r + dr[dist]
        next_c = c + dc[dist]

        if next_r < 0 or next_r >= n or next_c < 0 or next_c >= n or answer[next_r][next_c] != 0:
            dist = (dist+1) % 4

            next_r = r + dr[dist]
            next_c = c + dc[dist]
        r, c = next_r, next_c
        
    return answer