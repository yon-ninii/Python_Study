import sys

N = int(input().strip())
people = {}
for i in range(N):
    x, y = map(int, sys.stdin.readline().strip().split())
    people[(x, y, i)] = 1

k = list(people.keys())

for i in range(N):
    for j in range(N):
        if i == j: continue
        elif k[i][0] < k[j][0] and k[i][1] < k[j][1]: people[k[i]] += 1

for v in people.values():
    print(v, end = ' ')