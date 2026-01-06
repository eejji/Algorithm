def solution(myString, pat):
    new = ""
    for i in myString:
        if i == "A":
            new+= "B"
        else:
            new+="A"
    if pat in new:
        return 1
    else : return 0
