def solution(survey, choices):

    choice_dict = {
        1:3, # 매우 비동의
        2:2, # 비동의 
        3:1, # 약간 비동의
        4:0, # 모르겠음
        5:1, # 약간 동의
        6:2, # 동의
        7:3 # 매우 동의
    }

    survey_dict = {
        "R":0, "T":0,
        "C":0, "F":0,
        "J":0, "M":0,
        "A":0, "N":0
    }

    for i in range(len(choices)):
        if choices[i] > 4:
            survey_dict[survey[i][1]]+=choice_dict[choices[i]]
        elif choices[i] < 4:
            survey_dict[survey[i][0]]+=choice_dict[choices[i]]
        else:
            pass

    answer = ""
    # 1번 지표: R vs T
    if survey_dict["R"] >= survey_dict["T"]:
        answer += "R"
    else:
        answer += "T"

    # 2번 지표: C vs F
    if survey_dict["C"] >= survey_dict["F"]:
        answer += "C"
    else:
        answer += "F"

    # 3번 지표: J vs M
    if survey_dict["J"] >= survey_dict["M"]:
        answer += "J"
    else:
        answer += "M"

    # 4번 지표: A vs N
    if survey_dict["A"] >= survey_dict["N"]:
        answer += "A"
    else:
        answer += "N"

    return answer
