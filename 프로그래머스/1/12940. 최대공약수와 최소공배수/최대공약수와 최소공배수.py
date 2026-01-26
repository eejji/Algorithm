import math

def solution(n, m):
    
    for j in range(max(n, m), (n * m) + 1):
        if j % n == 0 and j % m == 0:
            b = j
            break
    
    return [math.gcd(n, m), b]


