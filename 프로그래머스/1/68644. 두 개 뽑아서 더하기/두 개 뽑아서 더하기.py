def solution(numbers):
    new = []
    for i in range(len(numbers)):
        for j in range(i, len(numbers)):
            if i == j:
                pass
            else:
                new.append(numbers[i]+numbers[j])
    return sorted(list(set(new)))