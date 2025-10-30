def solution(num_list):
    a, b = '', ''
    for i in num_list:
        if i % 2 == 0:
            a+=str(i)
        else:
            b+=str(i)
            
    return int(a)+int(b)