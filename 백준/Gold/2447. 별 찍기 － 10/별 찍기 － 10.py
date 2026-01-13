N = int(input())
stars = [['*' for _ in range(N)] for _ in range(N)]

def solve(x, y ,n):
    m = n // 3
    if n == 1:
        return

    for i in range(x + m, x + 2 * m):
        for j in range(y + m, y + 2 * m):
            stars[i][j] = ' '

    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            else:
                solve(x + i * m , y + j * m, m)

solve(0, 0, N)

for row in stars:
    print("".join(row))