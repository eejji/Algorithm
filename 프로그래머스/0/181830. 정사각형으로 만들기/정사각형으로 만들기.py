def solution(arr):
    if len(arr) > len(arr[0]):
        n = len(arr) - len(arr[0])
        for i in range(len(arr)):
            for j in range(n):
                arr[i].append(0)
        return arr
    
    elif len(arr) < len(arr[0]):
        n = len(arr[0]) - len(arr)
        for i in range(n):
            arr.append([0 for i in range(len(arr[0]))])
        return arr
    else:
        return arr