def recursion(st, l, r):
    global count
    count +=1

    if l >= r:
        return 1
    else:
        if st[l] != st[r]:
            return 0

    return recursion(st, l+1, r-1)


def isPalindrom(st):
    global count
    count = 0
    return recursion(st, 0, len(st)-1)


T = int(input())
for _ in range(T):
    S = input().strip()
    result = isPalindrom(S)
    print(result, count)