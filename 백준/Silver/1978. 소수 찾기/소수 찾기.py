import sys

n = int(input())
nums = list(map(int, sys.stdin.readline().strip().split()))

answer = 0

def is_prime(n):
    if n == 1: return True
    elif n == 2 or n == 3: return False
    a = int(n ** 0.5) + 1
    for i in range(2, a):
        if n % i == 0: return True
    return False

for i in range(n):
    if not is_prime(nums[i]): answer += 1

print(answer)
