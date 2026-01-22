def solution(n):
    new = ""
    for i in range(n):
        if i % 2 == 0:
            new+="수"
        else:
            new+="박"
    return new