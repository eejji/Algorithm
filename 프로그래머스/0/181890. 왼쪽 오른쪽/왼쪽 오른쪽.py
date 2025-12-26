def solution(str_list):
    a = []
    for i in range(len(str_list)):
        if str_list[i] == "l" or str_list[i] == "r":
            if str_list[i] == "l":
                a = str_list[:i]
                return a
            else:
                a = str_list[i+1:]
                return a
    return []