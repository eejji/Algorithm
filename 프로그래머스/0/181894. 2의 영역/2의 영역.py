def solution(arr):
    idx_li = []
    if 2 in arr:
        for i in range(len(arr)):
            if arr[i] == 2:
                idx_li.append(i)

        if idx_li:
            return arr[idx_li[0]:idx_li[-1]+1]
    else:
        idx_li.append(-1)
        return idx_li