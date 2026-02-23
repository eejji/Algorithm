import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    importance = list(map(int, input().split()))
    que = deque([(p, i) for i, p in enumerate(importance)])

    count =0
    
    while que:
        current = que.popleft() # que중 맨 앞에거 빼기
    
        if que and current[0] < max(que)[0]:
            que.append(current)
    
        else:
            count +=1
    
            if current[1] == m:
                print(count)
                break
