def solution(s, skip, index):
    answer = ""
    for i in s:
        x = ord(i)
        cnt = 0
        while cnt < index:
            x += 1

            if x > 122: # z검증
                x = 97

            if chr(x) in skip:
                continue

            cnt += 1
        answer += chr(x)

    return answer