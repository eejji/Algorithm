import sys

X = []

N = int(sys.stdin.readline())

for i in range(N):
    c = sys.stdin.readline().split()

    if c[0] == '1':
        X.append(int(c[1]))
        
    elif c[0] == '2':
        if X:
            print(X.pop())
        else:
            print(-1)
    
    elif c[0] == '3':
        print(len(X))
    
    elif c[0] == '4':
        if len(X) == 0:
            print(1)
        else:
            print(0)
    
    elif c[0] == '5':
        if X:
            print(X[-1])
        else:
            print(-1)