import math

T = int(input())

T_g = []
for i in range(T):
    a, b = map(int, input().split())
    g = math.gcd(a, b)
    l = a * b // g
    T_g.append(l)
    
for i in T_g:
    print(i)