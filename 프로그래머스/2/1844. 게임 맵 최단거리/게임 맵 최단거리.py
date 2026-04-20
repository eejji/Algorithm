from collections import deque

def solution(maps):
    
    n = len(maps)
    m = len(maps[0])
    
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    
    queue = deque([(0, 0)])
    
    while queue:
        y, x = queue.popleft()
        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            
            if 0 <= ny < n and 0 <= nx < m and maps[ny][nx] == 1:
                maps[ny][nx] = maps[y][x] + 1
                queue.append((ny, nx))
    
    answer = maps[n-1][m-1]
    return answer if answer > 1 else -1