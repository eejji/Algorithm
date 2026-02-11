while True:
    li = list(map(int, input().split()))

    if sum(li) == 0:
        break

    max_num = max(li)
    li.remove(max_num)

    if max_num**2 == li[0]**2 + li[1]**2:
        print('right')
    else:
        print('wrong')