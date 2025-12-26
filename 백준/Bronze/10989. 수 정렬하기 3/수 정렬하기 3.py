import sys
input = sys.stdin.readline


n = int(input())

li = [0 for _ in range(10001)]

for i in range(n):
    num = int(input())
    li[num] += 1

for i in range(len(li)):
    if li[i] != 0:
        for j in range(li[i]):
            print(i)