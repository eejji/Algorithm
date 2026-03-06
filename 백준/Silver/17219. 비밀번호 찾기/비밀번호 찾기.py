N, M = map(int, input().split())

L = {}

for i in range(N):
    a, b = input().split()
    L[a] = b
    
for i in range(M):
    c = input()
    print(L[c])