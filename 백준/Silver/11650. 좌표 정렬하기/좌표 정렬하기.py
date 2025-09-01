N = int(input())

points = []

for i in range(N):
    (a, b) = map(int, input().split())
    points.append((a,b))

points.sort()

for i in range(len(points)):
    print(points[i][0], points[i][1])