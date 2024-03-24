#p, q 
#p % q == 0 > 약수 

N, K = map(int, input().split())
a_li = []
for i in range(1,N+1,1):
    if N % i == 0:
        a_li.append(i)

if len(a_li) >= K:
    print(a_li[K-1])
else :
    print(0)