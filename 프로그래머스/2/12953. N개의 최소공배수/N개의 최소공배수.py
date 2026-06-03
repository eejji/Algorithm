import math

def solution(arr):

    answer = arr[0]

    for i in range(1, len(arr)):
        answer = math.lcm(answer, arr[i])

    return answer