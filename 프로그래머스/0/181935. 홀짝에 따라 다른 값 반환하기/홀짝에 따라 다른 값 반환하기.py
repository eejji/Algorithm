def solution(n):
    sum = 0
    if n % 2 == 0: # 짝수
        for j in range(2, n+1):
            if j % 2 == 0:
                print(j)
                sum += j**2
    else: # 홀수
        for j in range(1, n+1):
            if j % 2 != 0:
                sum += j
                
    return sum