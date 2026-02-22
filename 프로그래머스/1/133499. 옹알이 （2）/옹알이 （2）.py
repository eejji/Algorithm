def solution(babbling):
    answer = ["aya", "ye", "woo", "ma"]
    no_ans = ["ayaaya", "yeye", "woowoo", "mama"]
    cnt = 0

    for i in range(len(babbling)):

        is_valid = True
        for no in no_ans:
            if no in babbling[i]:
                is_valid = False
                break

        if is_valid:
            for a in answer:
                babbling[i] = babbling[i].replace(a, " ")

            if babbling[i].strip() == "":
                cnt +=1
    return cnt