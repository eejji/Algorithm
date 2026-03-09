zero = [1, 0] + [0] * 39
one = [0, 1] + [0] * 39

for i in range(2, 41):
    zero[i] = zero[i-1] + zero[i-2] # 1, 0
    one[i] = one[i-1] + one[i-2]

T = int(input())

for _ in range(T):
    N = int(input())
    print(f"{zero[N]} {one[N]}")


