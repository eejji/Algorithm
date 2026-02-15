def solution(price, money, count):
    
    total = sum([i for i in range(price,price*count+1,price)])

    if total > money:
        return total-money
    else:
        return 0