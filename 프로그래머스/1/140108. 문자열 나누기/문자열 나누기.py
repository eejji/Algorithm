def solution(s):
    answer = 0
    same = 0
    diff = 0
    x = ""

    for i in range(len(s)):
        if same == 0:
            x = s[i]
            same = 1
        else:
            if s[i] == x:
                same += 1
            else:
                diff += 1
        if same == diff:
            answer += 1
            same = 0
            diff = 0

    if same != 0:
        answer += 1
        
    return answer