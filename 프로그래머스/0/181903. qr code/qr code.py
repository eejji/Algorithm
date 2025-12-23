def solution(q, r, code):
    a = ''
    for i in range(len(code)):
        n = i % q
        if n == r:
            a += code[i]
    return a