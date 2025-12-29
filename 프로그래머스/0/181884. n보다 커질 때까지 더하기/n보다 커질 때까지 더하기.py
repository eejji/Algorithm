def solution(numbers, n):
    a = 0
    for i in range(len(numbers)):
        a += numbers[i]
        if n < a:
            b = numbers[:i+1]
            break
    
    return sum(b)