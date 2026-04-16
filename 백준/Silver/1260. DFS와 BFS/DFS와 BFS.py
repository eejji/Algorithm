import sys
from collections import deque

input_data = sys.stdin.read().split()
if not input_data:
    exit()

n, m, v = map(int, input_data[:3])

graph = [[] for _ in range(n + 1)]
pointer = 3

for _ in range(m):
    u = int(input_data[pointer])
    b = int(input_data[pointer + 1])
    graph[u].append(b)
    graph[b].append(u)
    pointer += 2

for i in range(1, n+1):
    graph[i].sort()

def dfs(node, visited):
    visited[node] = True
    print(node, end=' ')
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(neighbor, visited)

def bfs(start_node):
    visited = [False] * (n + 1)
    queue = deque([start_node])
    visited[start_node] = True

    while queue:
        node = queue.popleft()
        print(node, end = ' ')
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

visited_dfs = [False] * (n+1)
dfs(v, visited_dfs)
print()
bfs(v)


