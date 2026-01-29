from itertools import combinations


def solution(nums):
    cnt = 0

    for num in combinations(nums, 3):
        tmp = sum(num)
        for i in range(2, tmp):
            if tmp % i == 0:
                break
        else:
            cnt += 1

    return cnt