def solution(friends, gifts):
    name_gift = {}
    final_dict = {}
    gift_num = {}

    for i in friends:
        name_gift[i] = {}
        final_dict[i] = 0

        for j in friends:
            if i != j:
                name_gift[i][j] = 0

    for gift in gifts:
        giver, recevier = gift.split()
        name_gift[giver][recevier] += 1

    # 선물 지수 
    for i in friends:
        given = sum(name_gift[i].values())
        received = 0
        for j in friends:
            if i != j:
                received += name_gift[j][i]
        gift_num[i] = given - received

    for i in range(len(friends)):
        for j in range(i + 1, len(friends)): 
            p1 = friends[i]
            p2 = friends[j]

            if name_gift[p1][p2] > name_gift[p2][p1]:
                final_dict[p1] += 1
            elif name_gift[p1][p2] < name_gift[p2][p1]:
                final_dict[p2] += 1
            else:
                if gift_num[p1] > gift_num[p2]:
                    final_dict[p1] += 1
                elif gift_num[p1] < gift_num[p2]:
                    final_dict[p2] += 1

    return(max(final_dict.values()))