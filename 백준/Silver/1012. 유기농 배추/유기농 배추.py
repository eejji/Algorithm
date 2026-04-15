import sys
sys.setrecursionlimit(10000)

def clear_cluster(col, row):
    if col < 0 or col >= N or row < 0 or row >= M or not farm[col][row]:
        return
    farm[col][row] = False

    clear_cluster(col - 1, row)
    clear_cluster(col + 1, row)
    clear_cluster(col, row -1)
    clear_cluster(col, row + 1)

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())

    farm = [[False] * M for _ in range(N)]

    for _ in range(K):
        x, y = map(int, input().split())
        farm[y][x] = True

    # 메인 로직
    earthworms = 0
    for col in range(N):
        for row in range(M):
            if farm[col][row]:
                earthworms += 1
                clear_cluster(col, row)

    print(earthworms)