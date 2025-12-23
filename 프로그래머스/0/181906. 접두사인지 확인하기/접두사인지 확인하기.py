def solution(my_string, is_prefix):
    str_li = []
    for i in range(len(my_string)):
        str_li.append(my_string[:i])
                   
    if is_prefix in str_li:
        return(1)
    else: return(0)