from collections import Counter

num = [int(input()) for _ in range(3)]
number = num[0]*num[1]*num[2]

b = Counter(list(str(number)))

answer = [0] * 10

for i in b.keys():
    answer[int(i)]=b[i]

for i in answer:
    print(i)