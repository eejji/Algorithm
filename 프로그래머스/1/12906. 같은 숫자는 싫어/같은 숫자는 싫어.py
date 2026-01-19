def solution(arr):
    new = []
    new.append(arr[0])


    for i in range(1, len(arr)):
        if arr[i] != new[-1]:
            new.append(arr[i])
    return new

print(solution)