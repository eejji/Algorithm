N, score = map(int, input().split())
card = map(int, input().split())

card_li = sorted(card)
sub_li = []

for i in range(len(card_li)):
    #print(i, end=' ')
    for j in range(i+1,len(card_li)):
        #print(j, end=' ')
        for k in range(j+1, len(card_li)):
            #print(i, j, k)
            summation = card_li[i] + card_li[j] + card_li[k]
            if  summation <= score:
                sub_li.append(summation)
            else :
                pass
print(max(sub_li))