import sys
INF = 5001

N = int(input().strip())
P = list(map(int, sys.stdin.readline().strip().split()))
M = int(input().strip())
dp = [-INF for _ in range(M + 1)]
for i in range(N - 1, -1, -1):
    x = P[i]
    for j in range(x, M + 1):
        dp[j] = max(dp[j - x] * 10 + i, i, dp[j])

print(dp[M])