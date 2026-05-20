def 약수(n):
    if n == 1:
        return 0

    d = []
    for i in range(1, int(n**(1/2)) + 1):
        if n % i == 0:
            d.append(i)
            if i ** 2 != n:
                d.append(n//i)
    d.sort()
    d.pop()

    while d:
        val = d.pop()
        if val<= 10000000:
            return val

    return 1

def solution(begin, end):

    tmp = [1] * (end - begin + 1)

    if begin == 1:
        tmp[0] = 0

    for x in range(begin, end + 1):
        tmp[x - begin] = 약수(x)

    return tmp




