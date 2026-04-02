def solution(bandage, health, attacks):
    max_hp = health
    attacks_dict = {t: dmg for t, dmg in attacks}

    band_cnt = 0
    last_time = attacks[-1][0]

    for i in range(1, last_time + 1):
        if i in attacks_dict:
            health -= attacks_dict[i]
            band_cnt = 0

            if health <= 0:
                return -1
        else:
            health += bandage[1]
            band_cnt += 1

            if band_cnt == bandage[0]:
                health += bandage[2]
                band_cnt = 0

            if health > max_hp:
                health = max_hp

    return health