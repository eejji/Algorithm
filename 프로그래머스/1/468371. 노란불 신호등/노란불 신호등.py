import math
def lcm(a, b):
    return a * b // math.gcd(a, b)

def solution(signals):

    cycle_limit = 1

    for G, Y, R in signals: # signals 숫자만큼 여러번 돌리면서 최소 공배수 찾기
        cycle_limit = lcm(cycle_limit, G + Y + R)

    for time in range(1, cycle_limit+1):
        ok = True

        for G, Y, R in signals:
            cycle = G + Y + R
            t_mod = (time - 1) % cycle

            if not (G <= t_mod < G + Y):
                ok = False
                break

        if ok:
            return time
    return -1