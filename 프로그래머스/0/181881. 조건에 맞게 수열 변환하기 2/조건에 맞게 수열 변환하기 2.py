def cal(arr):
    for i in range(len(arr)):

        if arr[i] >= 50:
            if arr[i] % 2 ==0:
                arr[i] = arr[i] // 2

        else:
            if arr[i] % 2 != 0:
                arr[i] = (arr[i] * 2) + 1
    return arr

def solution(arr):
    an = arr.copy()
    n = 0

    while True:
        arr = cal(arr)

        if arr != an:
            an = arr.copy()
            n+=1
        else:
            break
            
    return n