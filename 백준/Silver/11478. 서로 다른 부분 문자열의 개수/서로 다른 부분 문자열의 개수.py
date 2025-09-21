S = input()
li = set()
for i in range(len(S)):
    for j in range(i, len(S)):
        li.add(S[i:j+1])

print(len(li))