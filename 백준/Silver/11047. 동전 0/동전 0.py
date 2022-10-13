import sys

N, K = map(int, sys.stdin.readline().strip().split())
coins = []
for _ in range(N):
    coins.append(int(sys.stdin.readline().strip()))
def match(c, m, cnt):
    max_c = c[0]
    for i in range(1, N):
        if c[i] <= m: max_c = c[i]
        elif c[i] > m:
            max_c = c[i - 1]
            break
    t_cnt = m // max_c
    m -= t_cnt * max_c
    return m, cnt + t_cnt
cnt = 0
while K != 0:
    K, cnt = match(coins, K, cnt)

print(cnt)