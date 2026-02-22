def solution(ingredient):
    stacks = []
    cnt = 0
    for ingre in ingredient:
        stacks.append(ingre)

        if stacks[-4:] == [1,2,3,1]:
            for _ in range(4):
                stacks.pop()
            cnt+=1
    return cnt