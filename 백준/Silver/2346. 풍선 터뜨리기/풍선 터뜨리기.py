from collections import deque

N = int(input())
moves = list(map(int, input().split()))

dq = deque((i+1, moves[i]) for i in range(N))
result = []

while dq:
    idx, move = dq.popleft()
    result.append(idx)
    if dq:
        if move > 0:
            dq.rotate(-(move - 1))
        else:
            dq.rotate(-move)

for i in result:
    print(i, end=' ')
