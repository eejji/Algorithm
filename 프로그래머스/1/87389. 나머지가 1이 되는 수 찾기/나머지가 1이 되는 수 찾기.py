def solution(n):
    cnt=1
    while True:
        if n % cnt == 1:
            break
        else:
            cnt+=1
    return cnt