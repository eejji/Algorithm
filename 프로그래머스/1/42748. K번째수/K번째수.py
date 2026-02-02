def solution(array, commands):
    new = []
    for i, j, k in commands:
        new.append(sorted(array[i-1:j])[k-1])
    return new