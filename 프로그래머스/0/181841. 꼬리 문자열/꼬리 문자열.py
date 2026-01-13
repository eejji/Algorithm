def solution(str_list, ex):
    sol = ""
    for i in str_list:
        if ex not in i:
            sol+= i
    return sol