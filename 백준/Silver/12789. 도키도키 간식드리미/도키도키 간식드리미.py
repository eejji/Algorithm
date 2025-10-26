n = int(input())
c_number = list(map(int, input().split()))

stack = []
target = 1

for num in c_number:
    stack.append(num)
    # 스택의 top이 현재 목표 번호면 계속 pop
    while stack and stack[-1] == target:
        stack.pop()
        target += 1

if not stack:
    print("Nice")
else:
    print("Sad")
