def solution(number, limit, power):
    counts = [0] * (number + 1)
    
    for i in range(1, number + 1):
        for j in range(i, number + 1, i):
            counts[j] += 1
            
    ans = 0
    for i in range(1, number + 1):
        c = counts[i]
        ans += c if c <= limit else power
    return ans