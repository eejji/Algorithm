def solution(absolutes, signs):
    new = []
    for i in range(len(signs)):
        if signs[i]:
            new.append(absolutes[i])
        else:
            new.append(int('-'+str(absolutes[i])))
    return sum(new)