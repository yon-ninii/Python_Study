import sys

N, M = map(int, input().strip().split())
nums = list(map(int, sys.stdin.readline().strip().split()))

_max = 0

for i in range(N - 2):
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            n = nums[i] + nums[j] + nums[k]
            if n <= M and n > _max: _max = n

print(_max)
