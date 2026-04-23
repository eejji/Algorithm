def solution(n):
    answer = ''
    
    numbers = ['4', '1', '2']
    
    while n > 0:
        remainder = n % 3
        n = n // 3
        
        if remainder == 0:
            n -= 1
            
        answer = numbers[remainder] + answer
        
    return answer