n, m = map(int, input().split())

s = []
def back(start, N, M): # 시작 정보
    if len(s) == M:
        print(" ".join(map(str, s)))
        return

    for i in range(start, N+1): # start부터 m+1까지 해야 1~3이렇게 할 수 있음
        s.append(i)
        back(i, N, M)
        s.pop()

back(1, n, m)