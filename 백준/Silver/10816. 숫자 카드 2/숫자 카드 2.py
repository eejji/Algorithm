N = int(input())
cards = list(map(int, input().split()))

M = int(input())
cards2 = list(map(int, input().split()))

count = {}
for card in cards:
    if card in count:
        count[card] += 1
    else:
        count[card] = 1
        
for target in cards2:
    result = count.get(target)
    if result == None:
        print(0, end= " ")
    else:
        print(result, end= " ")