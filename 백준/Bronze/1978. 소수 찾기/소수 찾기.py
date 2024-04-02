# 소수는 약수가 1이랑 자기 자신만 있는 것을 뜻함
N = int(input())
data = list(map(int, input().split()))
count =0 

for x in data:
    for i in range(2, x+1):
        if x % i ==0:
            if x == i:
                count += 1
            break

            
print(count)