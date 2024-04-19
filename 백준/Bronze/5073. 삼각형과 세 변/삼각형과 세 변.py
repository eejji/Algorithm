while 1:
    a, b, c = map(int, input().split())
    if a == 0:
        break
    max_ = max(a,b,c)
    if a + b + c - max_ <= max_:
        print("Invalid")
    elif a == b == c:
        print("Equilateral")
    elif a == b or b == c or a == c:
        print("Isosceles")
    elif a != b != c:
        print("Scalene")