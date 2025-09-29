def is_prime(num):
    if num < 2: return False
    if num == 2: return True
    if num % 2 == 0: return False
    for i in range(3, int(num**0.5)+1, 2):  # 홀수만
        if num % i == 0:
            return False
    return True

n = int(input())
n_li = []

for i in range(n):
    x = int(input())

    while True:
        if is_prime(x):
            break
        x += 1        
        
    n_li.append(x)

for i in n_li:
    print(i)