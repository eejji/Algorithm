def solution(s):
    new_ss = []
    ss = s.split(" ")
    for i in ss:
        converted = "".join([i[j].upper() if j % 2 == 0 else i[j].lower() for j in range(len(i))])
        new_ss.append(converted)
    return " ".join(new_ss)