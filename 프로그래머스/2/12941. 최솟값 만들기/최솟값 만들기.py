def solution(a,b):
    a.sort()
    b.sort(reverse=True)
    s = 0
    for x, y in zip(a, b):
        s+= (x * y)
    return s
