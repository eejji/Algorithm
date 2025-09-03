N = int(input())

str_list = []
for i in range(N):
    str_list.append(input())

new_str_list1 = list(set(str_list))
new_str_list1.sort()
new_str_list1.sort(key=len)

for i in new_str_list1:
    print(i)