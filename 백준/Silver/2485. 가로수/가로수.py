import math 

N = int(input())

num_li = []

for i in range(N):
    num_li.append(int(input()))
    
gaps = []
for i in range(1, N):
    gaps.append(num_li[i] - num_li[i-1])
    
g = gaps[0]

for gap in gaps[1:]:
    g = math.gcd(g, gap)
    
sum_n = 0
for j in gaps:
    sum_n += int((j/g)-1)
    
print(sum_n)