N = int(input())

name_list = []

for i in range(N):
    name_list.append(input().split())

name_list.sort(key=lambda x: int(x[0]))

for i in range(len(name_list)):
    print(name_list[i][0], name_list[i][1])