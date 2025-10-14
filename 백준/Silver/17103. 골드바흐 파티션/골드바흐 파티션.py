import math

def make_prime_table(max_num):
    is_prime = [True] * (max_num + 1)
    is_prime[0] = is_prime[1] = False

    # max_num이 20이라고 가정할 때 소수는 2, 3, 5만 있음 그래서 for문은 2, 3, 5만 순회
    for i in range(2, int(math.sqrt(max_num)) + 1):  
        if is_prime[i]:
            for j in range(i * i, max_num+1, i):
                is_prime[j] = False

    return is_prime
            
is_prime = make_prime_table(1000000)

T = int(input())

for _ in range(T):
    n = int(input())
    count = 0

    for i in range(2, n //2 +1):
        if is_prime[i] and is_prime[n-i]:
            count += 1
    print(count)