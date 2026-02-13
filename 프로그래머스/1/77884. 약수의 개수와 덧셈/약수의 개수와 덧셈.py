def cal2(num):
    count = 0
    for i in range(1, num+1):
        if num % i == 0:
            count += 1
    return count % 2 == 0

def solution(left, right):
    ss = 0
    for n in range(left, right+1):
        if cal2(n):
            ss += n
        else:
            ss -= n
    return ss