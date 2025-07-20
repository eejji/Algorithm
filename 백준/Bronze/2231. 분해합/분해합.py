N = int(input())

start = max(1, N - 9 * len(str(N)))

for M in range(start, N):
    digit_sum = sum(int(d) for d in str(M))
    if M + digit_sum == N:
        print(M)
        break
else:
    print(0)