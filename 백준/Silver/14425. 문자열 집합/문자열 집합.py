a, b = input().split()
a, b = int(a), int(b)

s = []
for i in range(a):
    s.append(input())

m = []
for i in range(b):
    m.append(input())

number = 0
for i in range(len(m)):
    if m[i] in s:
        number += 1

print(number)