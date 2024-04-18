N = int(input())
X, Y = [], []
for i in range(N):
    x, y = map(int, input().split())
    X.append(x); Y.append(y)

if len(X) < 2:
    print(0)
else: print((max(X)-min(X)) * (max(Y)-min(Y)))
