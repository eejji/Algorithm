from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
M = int(input())
C = list(map(int, input().split()))

dq = deque()

# 1) 큐(0)인 자료구조에 있던 초기 값들만 모은다
for i in range(N):
    if A[i] == 0:
        dq.append(B[i])

# 2) 새로 들어오는 값 C[j]를 왼쪽에 넣고, 오른쪽에서 뺀 값을 출력
ans = []
for x in C:
    dq.appendleft(x)     # 새로 들어오는 값
    out = dq.pop()       # 최종적으로 빠져나오는 값
    ans.append(out)

print(*ans)
