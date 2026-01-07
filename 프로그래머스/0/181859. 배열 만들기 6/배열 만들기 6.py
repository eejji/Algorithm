def solution(arr):
    i = 0
    stk = []

    while i < len(arr):
        if len(stk) < 1:
            stk.append(arr[i])
            i+=1
        elif len(stk) >= 1 and stk[-1] == arr[i]:
            stk.pop(-1)
            i+=1
        elif len(stk) >= 1 and stk[-1] != arr[i]:
            stk.append(arr[i])
            i+=1
    if stk:
        return stk
    else:
        return [-1]