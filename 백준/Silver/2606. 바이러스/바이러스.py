n = int(input())
computer = int(input())

graph = [[] for _ in range(n+1)]

for _ in range(computer):
    s = input().split()
    u, v = int(s[0]), int(s[1])

    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (n+1)
queue = [1]
visited[1] = True

count = 0

while queue:

    current = queue.pop(0)

    for neighbor in graph[current]:
        if visited[neighbor] == False:
            visited[neighbor] = True
            queue.append(neighbor)
            count+=1

print(count)