from collections import Counter

def counter(li):

    li2 = []
    for i in li:
        li2.append(i.split()[1])

    dict = Counter(li2)

    result = 1
    for key in dict:
        result *= (dict[key] + 1)

    result -= 1

    return result

t = int(input())

for _ in range(t):
    n = int(input()) # 의상 수 
    li = []
    for _ in range(n):
        a, b = input().split() # 의상의 이름 // 의상의 종류
        li.append(a + " " + b)

    print(counter(li))
