# 9095. 1, 2, 3 더하기

n = int(input())

dp = [0 for i in range (12)]
result = [0 for i in range (n)]

dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range (4, 12):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for i in range(n):
    result[i] = dp[int(input())]
    
for i in range(n):
    print(result[i])
