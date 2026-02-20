def solution(X, Y):
    answer = ''


    for i in range(9, -1, -1):
        char = str(i)

        count = min(X.count(char), Y.count(char))
        answer += char * count


    if not answer:
        return "-1"
    if answer[0] == "0":
        return "0"

    return answer