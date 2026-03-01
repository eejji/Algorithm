import sys
input = sys.stdin.readline

n = int(input())
stack = []
ans = []
cur = 1
possible = True

for _ in range(n):
    num = int(input())
    
    while cur <= num:
        stack.append(cur)
        ans.append('+')
        cur += 1
        
    if stack[-1] == num:
        stack.pop()
        ans.append('-')
    else:
        possible = False
        break

if not possible:
    print("NO")
else:
    print('\n'.join(ans))