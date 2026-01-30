def solution(n, arr1, arr2):

    for i in range(len(arr1)):
        arr1[i] = bin(arr1[i])[2:].zfill(n)
        arr2[i] = bin(arr2[i])[2:].zfill(n)

    final = []

    for r1, r2 in zip(arr1, arr2):
        row_result =""

        for c1, c2 in zip(r1, r2):
            if c1 == '1' or c2 == '1':
                row_result += "#"
            else:
                row_result += " "

        final.append(row_result)
        
    return final