def solution(d, budget):
    dd = sorted(d)

    i = 0
    cnt = 0

    while i < len(dd) and budget >= dd[i]:
        budget -= dd[i]
        cnt += 1
        i += 1
        
    return cnt