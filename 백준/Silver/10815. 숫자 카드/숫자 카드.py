n = int(input())
n_list = input().split()

m = int(input())
m_list = input().split()

aa = set(n_list)

for x in m_list:
    print(1 if x in aa else 0, end= ' ')