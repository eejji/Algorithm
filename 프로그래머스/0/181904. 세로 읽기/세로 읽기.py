def solution(my_string, m, c):
    num = 0
    f_li = []
    t_li = []
    result=''

    for i in range(len(my_string)):
        f_li.append(my_string[i])
        num += 1
        if num % ｍ == 0:
            t_li.append(f_li)
            f_li = []

    for i in range(len(t_li)):
        result += t_li[i][c-1]
        
    return result