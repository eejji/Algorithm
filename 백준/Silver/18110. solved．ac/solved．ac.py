import sys

def my_round(val):
    if val - int(val) >= 0.5:
        return int(val) + 1
    else:
        return int(val)

input = sys.stdin.readline
n = int(input())

if n == 0:
    print(0)
else:
    num = [int(input()) for _ in range(n)]
    num.sort()

    exclude = my_round(n * 0.15)

    a = num[exclude : n - exclude]

    print(my_round(sum(a) / len(a)))