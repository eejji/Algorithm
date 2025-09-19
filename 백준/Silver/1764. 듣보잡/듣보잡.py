N, M = map(int, input().split())

N_list = []
M_list = []

for i in range(N):
    N_list.append(input())

N_list = set(N_list)

M_list = []
for j in range(M):
    name = input()
    if name in N_list:
        M_list.append(name)

M_list.sort()
print(len(M_list))
for i in M_list:
    print(i)