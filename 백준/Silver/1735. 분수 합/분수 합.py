import math

a, b = map(int, input().split())
c, d = map(int, input().split())

e = a * d + b * c  # 분자
f = b * d  # 분모 

g = math.gcd(e, f)

print(e // g, f // g)