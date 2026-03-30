import sys
input = sys.stdin.readline

n, m = map(int, input().split())
numbers = list(map(int, input().split()))

prefix = [0]

for num in numbers:
    prefix.append(prefix[-1] + num)

for _ in range(m):
    start, end = map(int, input().split())
    print(prefix[end] - prefix[start - 1])