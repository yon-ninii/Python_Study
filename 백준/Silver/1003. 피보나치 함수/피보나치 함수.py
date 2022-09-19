import sys

T = int(input().strip())
answer = []
for _ in range(T):
    N = int(sys.stdin.readline().strip())
    if N == 0:
        answer.append([1, 0])
        continue
    elif N == 1:
        answer.append([0, 1])
        continue
    DP = {}
    for i in range(N + 1): DP[i] = [0, 0]
    DP[0] = [1, 0]
    DP[1] = [0, 1]
    f = 2
    while f <= N:
        a, b = DP[f]
        a += DP[f - 1][0] + DP[f - 2][0]
        b += DP[f - 1][1] + DP[f - 2][1]
        DP[f] = [a, b]
        f += 1
    answer.append(DP[N])
for a, b in answer:
    print(a, b)
