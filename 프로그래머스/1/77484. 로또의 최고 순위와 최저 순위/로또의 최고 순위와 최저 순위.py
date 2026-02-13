def solution(lottos, win_nums):
    cnt = 0
    z_cnt = 0

    reward ={6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}

    for i in range(len(lottos)):
        if lottos[i] == 0:
            z_cnt += 1
        for j in range(len(win_nums)):
            if lottos[i] == win_nums[j]:
                cnt+=1

    return [reward[cnt+z_cnt], reward[cnt]]