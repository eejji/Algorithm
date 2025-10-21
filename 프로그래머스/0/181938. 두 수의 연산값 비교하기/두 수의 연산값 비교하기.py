def solution(a, b):
    num = int(str(a) + str(b))
    if num < 2 * a * b:
        return 2 * a * b
    elif num == 2 * a * b:
        return num
    else:
        return num