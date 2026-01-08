def solution(arr):
    answer = [2**i for i in range(11)]
    while len(arr) not in answer :
        arr.append(0)
    return arr