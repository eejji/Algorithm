K = int(input())

stack = []
for i in range(K):
    N = int(input())

    if N == 0:
        stack.pop()

    else:
        stack.append(N)

sum = 0

for i in stack:
    sum+= i 

print(sum)