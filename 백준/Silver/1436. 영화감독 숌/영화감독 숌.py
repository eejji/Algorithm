N = int(input())
i = 1
cnt = 0

while True:
    i += 1
    if '666' in str(i):
        cnt += 1
    if cnt == N:
        print(i)
        break