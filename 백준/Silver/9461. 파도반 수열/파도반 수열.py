T = int(input())
nums = [int(input()) for _ in range(T)]
max_n = max(nums)
dp = [0] * (max_n + 1)

dp[1] = 1
dp[2] = 1
dp[3] = 1
dp[4] = 2
dp[5] = 2
for i in range(6, max_n+1):
    dp[i] = dp[i-2] + dp[i-3]
    
for n in nums:
    print(dp[n])