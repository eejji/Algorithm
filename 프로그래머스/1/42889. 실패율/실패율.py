from collections import Counter

def solution(N, stages):
    c_stage = Counter(stages)
    total_players = len(stages)
    ratio = []
    
    for i in range(1, N+1): 
        if total_players == 0:
            r = 0
        else:
            r = c_stage[i] / total_players
            total_players -= c_stage[i]
        ratio.append((i, r))

    result = sorted(ratio, key=lambda x: (-x[1], x[0]))
    return [i[0] for i in result]