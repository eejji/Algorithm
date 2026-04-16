def solution(n, w, num):

    t = []
    total = []
    for i in range(1, n+1): # 1 ~ 22
        t.append(i)
        if len(t) == w:
            if len(total) % 2 == 1:
                total.append(t[::-1])
            else:
                total.append(t)
            t = []
    while len(t) < w:
        t.append(0)

    if len(total) % 2 == 1:
        total.append(t[::-1])
    else:
        total.append(t)

    target_row = -1
    target_col = -1

    # number 찾기
    for i in range(len(total)):
        for j in range(len(total[i])):
            if total[i][j] == num:
                target_row = i
                target_col= j
                break

    count = 0
    for k in range(target_row, len(total)):
        if total[k][target_col] != 0:
            count +=1

    return count