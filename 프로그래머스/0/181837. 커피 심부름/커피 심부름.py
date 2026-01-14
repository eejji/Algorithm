def solution(order):

    
    lattee = ["icecafelatte", "cafelatteice", "hotcafelatte", "cafelattehot", "cafelatte"]
    
    sum = 0
    for name in order:
        if name in lattee:
            sum += 5000
        else:
            sum += 4500

    return sum