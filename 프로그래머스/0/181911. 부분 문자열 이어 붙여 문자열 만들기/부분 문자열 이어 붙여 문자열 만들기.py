def solution(my_strings, parts):
    answer = ''
    for idx, s in enumerate(my_strings):
        answer += my_strings[idx][parts[idx][0]:parts[idx][1]+1]
    return answer

