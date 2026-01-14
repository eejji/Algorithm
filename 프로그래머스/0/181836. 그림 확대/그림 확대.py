def solution(picture, k):
    x_li = []
    for i in range(len(picture)):
        x_li.append("".join([i*k for i in picture[i]]))

    y_li = []
    for i in x_li:
        for _ in range(k):
            y_li.append(i)
    return y_li