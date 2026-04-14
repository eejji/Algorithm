import sys
import math
input = sys.stdin.readline

n = int(input())
# 제곱수 의 합

dp = [0] * (n+1)

dp[0] = 0 # 0은 제곱해도 무조건 0이니까 0
dp[1] = 1 # 1도 제곱해도 무조건 1이니까 1 


for i in range(2, n+1): # 입력된 숫자만큼 순회하려는 for문
    dp[i] = float('inf') # 
    for j in range(1, int(math.sqrt(i)) + 1):
        dp[i] = min(dp[i], dp[i-j*j]+1)


print(dp[n])