def solution(k, m, score):
    score.sort(reverse=True)

    total = 0

    for i in range(m-1, len(score), m):
        total += score[i] * m
    
    return total