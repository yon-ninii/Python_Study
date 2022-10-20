import sys

N = int(input().strip())
coor = list(map(int, sys.stdin.readline().strip().split()))
s = sorted(list(set(coor)))
d = {}
for i in range(len(s)):
    d[s[i]] = i
answer = []
for i in range(N):
    answer.append(d[coor[i]])
for i in range(N):
    print(answer[i], end = ' ')