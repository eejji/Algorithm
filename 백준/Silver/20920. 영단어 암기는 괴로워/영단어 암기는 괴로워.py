import sys
from collections import Counter


input = sys.stdin.readline


N, M = map(int, input().split())


a = [input().strip() for _ in range(N)]

b = [i for i in a if len(i) >= M]

c = Counter(b)
sorted_list = sorted(c.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

for word, count in sorted_list:
    sys.stdout.write(word + '\n') 