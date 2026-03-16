def to_days(data_str):
    y, m, d = map(int, data_str.split('.'))
    return (y * 12 * 28) + (m * 28) + d

def solution(today, terms, privacies):

    terms_dic = {}
    today_days = to_days(today)
    answer = []

    for i in range(len(terms)):
        a, b = terms[i].split()
        terms_dic[a] = int(b)

    for i in range(len(privacies)):
        a, b = privacies[i].split()

        if to_days(a) + terms_dic[b] * 28 <= today_days:
            answer.append(i+1)

    return answer