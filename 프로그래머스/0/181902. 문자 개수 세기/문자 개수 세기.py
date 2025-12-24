def solution(my_string):
    answer = [0] * 52
    
    for s in my_string:
        if s.isupper():
            idx = ord(s) - 65
        else:
            idx = ord(s) - 97 + 26
        answer[idx] += 1

    return answer