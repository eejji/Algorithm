def mul(a, b):
    s = 0
    for i in range(len(a)):
        s += a[i] * b[i]
    return s

def solution(arr1, arr2):

    result = []

    for i in range(len(arr1)): # 3회 순회
        sub_re = []
        for j in range(len(arr2[0])):
            col = [arr2[k][j] for k in range(len(arr2))]
            sub_re.append(mul(arr1[i], col))
        result.append(sub_re)

    return result
