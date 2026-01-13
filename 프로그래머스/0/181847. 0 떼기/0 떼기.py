def solution(n_str):
    a = [n_str[i] for i in range(len(n_str))]

    n = 0
    while True:
        if a[n] == '0':
            print(a)
            a.pop(0)
        else:
            break

    
    return "".join(a)
    