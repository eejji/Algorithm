import sys
input = sys.stdin.readline

N, K = map(int, input().split())
A = [int(input()) for _ in range(N)]
cnt=0
for i in range(len(A)-1, -1, -1):
    if K // A[i]:
        cnt += K//A[i]
        K = K%A[i]
    else:
        pass
print(cnt)