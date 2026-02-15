def solution(numbers):
    s = 0
    for i in range(1,10):
        if i not in numbers:
            s+=i
    return s