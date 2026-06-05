def solution(s):
    stacks = []

    for c in s:
        if stacks and stacks[-1] == c:
            stacks.pop()
        else:
            stacks.append(c)
    if len(stacks) == 0:
        return 1
    else:
        return 0