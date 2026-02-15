def solution(id_list, report, k):
    recall_ = {} # 유저별 처리 결과를 받은 횟수
    user_li = {} # 유저별 신고한 사람을 담는 거
    user_n = {}
    for i in range(len(id_list)):
        recall_[id_list[i]] = 0
        user_li[id_list[i]] = []
        user_n[id_list[i]] = 0


    for i in range(len(report)):
        user_id, user_to = report[i].split()
        user_li[user_id].append(user_to)

    for i in (list(user_li.keys())):
        user_li[i] = list(set(user_li[i]))

    a = list(user_li.values())
    for i in range(len(a)):
        for j in range(len(a[i])):
            user_n[a[i][j]]+=1

    names = []
    for i in list(user_n):
        if user_n[i] >= k:
            names.append(i)

    name = list(user_li.keys())
    for i in range(len(name)):
        val_user = user_li[name[i]]
        if len(val_user) == 0:
            recall_[name[i]] = 0
        else:
            for j in range(len(val_user)):
                if val_user[j] in names:
                    recall_[name[i]] += 1

    return list(recall_.values())