def solution(n, m, section):

    count = 0
    end = 0

    for s in section:
        if s > end:
            count += 1
            end = s + m -1
    
    return count