def cal_(a):
    for i in range(len(a) // 2):
        if a[i] != a[-1-i]:
            return False
    return True

while True:
    a = int(input())
    if a == 0:
        break
    if cal_(str(a)):
        print("yes")
    else:
        print("no")