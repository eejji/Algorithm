def cal(num):
    a = 0

    while num > 1:
        a+=1
        if num % 2 == 0:
            num = num //2
        else:
            num = (num-1)//2

    return a

def solution(num_list):
    n = 0
    for i in range(len(num_list)):
        n += cal(num_list[i])
    return n