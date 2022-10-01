import sys

N = int(input().strip())
A = list(map(int, sys.stdin.readline().strip().split()))
M = int(input().strip())
B = list(map(int, sys.stdin.readline().strip().split()))

A.sort()

def binary(a, m, end):
    mid, start = 0, 0
    while start != end:
        mid = (start + end) // 2
        if m == a[mid]: return 1
        elif m > a[mid]: start = mid + 1
        else: end = mid
    if a[start] == m: return 1
    return 0

for m in B:
    print(binary(A, m, N - 1))