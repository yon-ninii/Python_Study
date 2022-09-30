import sys

K, N = map(int, sys.stdin.readline().split())
Cable = []

for _ in range(K):
    Cable.append(int(sys.stdin.readline().strip()))

def find_length(k, n, cable):
    left, right = 1, max(cable)
    length = 0
    while left <= right:
        mid = (left + right) // 2
        num = 0

        for i in cable:
            num += i // mid

        if num >= n:
            left = mid + 1
            length = mid
        else:
            right = mid - 1

    return length

Result = find_length(K, N, Cable)
print(Result)
