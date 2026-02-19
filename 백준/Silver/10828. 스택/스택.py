import sys
N = int(sys.stdin.readline())

stacks = []
for _ in range(N):
    cmd = sys.stdin.readline().split()

    if cmd[0] == "push":
        stacks.append(int(cmd[1]))
    elif cmd[0] == "pop":
        if len(stacks) == 0:
            print(-1)
        else:
            a = stacks.pop()
            print(a)
    elif cmd[0] == "size":
        print(len(stacks))
    elif cmd[0] == "empty":
        if len(stacks) == 0:
            print(1)
        else:
            print(0)
    elif cmd[0] == "top":
        if len(stacks) == 0:
            print(-1)
        else:
            print(stacks[-1])