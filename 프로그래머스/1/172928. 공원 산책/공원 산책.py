def solution(park, routes):

    for i in range(len(park)):
        row = park[i]
        for j in range(len(row)):
            if row[j] == "S":
                current = (i, j)

    for i in range(len(routes)):
        op, n = routes[i].split()
        n = int(n)

        if op == "N":
            dx, dy = -1, 0
        elif op == "S":
            dx, dy = 1, 0
        elif op =="W":
            dx, dy = 0, -1
        elif op =="E":
            dx, dy = 0, 1

        x, y = current
        possible = True

        for _ in range(n):
            x += dx
            y += dy

            if x < 0 or x >= len(park) or y < 0 or y >= len(park[0]):
                possible = False
                break

            if park[x][y] == "X":
                possible = False
                break

        if possible:
            current = (x,y)
            
    return list(current)
