def solution(myString):
    new = []
    for i in range(len(myString)):
        if myString[i] < "l":
            new.append("l")
        else:
            new.append(myString[i])
    return "".join(new)