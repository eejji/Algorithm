def solution(number):
    from itertools import combinations
    answer=0
    all_teams = combinations(number,3)

    for team in all_teams:
        if sum(team) == 0:
            answer+=1

    return answer