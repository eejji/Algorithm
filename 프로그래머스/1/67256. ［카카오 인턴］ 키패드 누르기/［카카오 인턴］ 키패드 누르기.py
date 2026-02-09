def solution(numbers, hand):

    keypad = {1: (0,0), 2:(0,1), 3:(0,2),
              4: (1,0), 5:(1,1), 6:(1,2),
              7:(2,0), 8:(2,1), 9:(2,2),
              '*':(3,0), 0:(3,1), '#':(3,2)}

    def cal_distance(pos1, pos2):
        return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

    left_pos = (3,0)
    right_pos = (3,2)

    hands = ""
    for i in range(len(numbers)):
        if numbers[i] in [1, 4, 7]:
            left_pos = keypad[numbers[i]]
            hands+="L"
        elif numbers[i] in [3, 6, 9]:
            right_pos = keypad[numbers[i]]
            hands+="R"
        else:
            left_dis = cal_distance(keypad[numbers[i]], left_pos)
            print(keypad[numbers[i]], left_pos, left_dis)
            right_dis = cal_distance(keypad[numbers[i]], right_pos)
            print(keypad[numbers[i]], right_pos, right_dis)

            if left_dis == right_dis:
                if hand == "right":
                    hands+="R"
                    right_pos = keypad[numbers[i]]
                else:
                    hands+="L"
                    left_pos = keypad[numbers[i]]
            else:
                if left_dis > right_dis:
                    hands+="R"
                    right_pos = keypad[numbers[i]]
                else:
                    hands+="L"
                    left_pos = keypad[numbers[i]]
                    
    return hands