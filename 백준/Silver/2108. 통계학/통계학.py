import sys
from collections import Counter
input = sys.stdin.readline

# 입력
n = int(input())
lst = [int(input()) for i in range(n)]

# 1. 산술평균
print(round(sum(lst)/n))

# 2. 중앙값
lst.sort()
print(lst[n//2])

# 3. 최빈값
cnt = Counter(lst)
mode = cnt.most_common()

if len(mode) == 1 or mode[0][1] != mode[1][1]:
    print(mode[0][0])
else:
    print(mode[1][0])

# 4. 범위
print(max(lst)-min(lst))
