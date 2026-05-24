def solution(s):
    ss = [int(x) for x in s.split()]
    maxx, minn = max(ss), min(ss)
    return f"{minn} {maxx}"
    #print(f"{minn} {maxx}")