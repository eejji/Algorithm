T = int(input())

for i in range(T):
    H, W, N = map(int, input().split())

    c = N % H
    ho = (N // H) + 1

    if c == 0:
        c = H
        ho -= 1

    print(c * 100 + ho)