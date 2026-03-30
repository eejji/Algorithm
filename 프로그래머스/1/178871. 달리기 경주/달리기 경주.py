def solution(players, callings):
    player_dict = {}

    for i in range(len(players)):
        player_dict[players[i]] = i

    for name in callings:
        current = player_dict[name]
        front_name = players[current - 1]

        # players에서 자리 교체
        players[current - 1], players[current] = players[current], players[current - 1]

        player_dict[name] = current - 1
        player_dict[front_name] = current
        
    return players