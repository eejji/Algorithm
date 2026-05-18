def solution(n):
    # 점화식 세우기
    # 1234567을 나눈 나머지 리턴

    nn = [0] * (n+1)

    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        # n에 도착하기 전에 1칸 남았을 때 
        nn[1] = 1

        # n에 도착하기 전에 2칸 남았을 때 
        nn[2] = 2


        for i in range(3, n+1):
            nn[i] = (nn[i-2] + nn[i-1]) % 1234567

        return nn[n]



