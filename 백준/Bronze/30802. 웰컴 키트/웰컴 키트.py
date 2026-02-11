N = int(input())
person = list(map(int, input().split()))
T, P = map(int, input().split())

a = 0
for i in person:
    if i == 0:
        continue
    elif i <= T:
        a +=1
    elif i % T == 0:
        a += (i//T)
    else:
        a += (i//T) + 1

print(a)
print(f'{N//P} {N%P}')