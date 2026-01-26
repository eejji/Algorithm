def solution(num):
    t = 0
    anw = 0
    n = num
    while True:
        if n == 1:
            anw = t
            break

        if t >= 500 :
            anw = -1
            break

        if n % 2 == 0:
            n = n //2
            t+=1
        else:
            n = n * 3 + 1
            t+=1
            
    return anw