def solution(k, score):

    answer = []
    stack = []

    for i in range(len(score)):
        if len(stack) == k:
            if score[i] <= min(stack):
                answer.append(min(stack))
            else:
                stack = sorted(stack)
                stack.pop(0)
                stack.append(score[i])
                answer.append(min(stack))
        else:
            stack.append(score[i])
            answer.append(min(stack))

    return answer