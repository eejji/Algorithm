import sys
from collections import deque

input = sys.stdin.readline

N = int(input()) # 명령 수 

Que = deque()

for i in range(N):
    cmd = input().split()

    if cmd[0] == 'push':
        Que.append(cmd[1])
        
    elif cmd[0] == 'pop':
        print(Que.popleft() if Que else -1)

    elif cmd[0] == 'size':
        print(len(Que))

    elif cmd[0] == 'empty':
        if len(Que) == 0:
            print(1)
        else:
            print(0)

    elif cmd[0] == 'front':
        print(Que[0] if Que else -1)

    elif cmd[0] == 'back':
        print(Que[-1] if Que else -1)
