def solution(a, b):
    s =0
    for x, y in zip(a, b):
        s+=x*y
    return s