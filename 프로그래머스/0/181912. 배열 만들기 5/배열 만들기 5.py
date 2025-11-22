def solution(intStrs, k, s, l):
    li = []
    for i in range(len(intStrs)):
        number = int(intStrs[i][s:s+l])
        if number > k:
            li.append(number)
        else:
            pass

    return li
