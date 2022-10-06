import sys
from itertools import combinations
from collections import deque
import copy

N, M = map(int, input().split())

lab = []
zero_x, zero_y = [], []
two_x, two_y = [], []

for i in range(N):
    l = list(map(int, sys.stdin.readline().split()))
    lab.append(l)
    for j in range(M):
        if l[j] == 0:
            zero_x.append(j)
            zero_y.append(i)
        elif l[j] == 2:
            two_x.append(j)
            two_y.append(i)

zeros = len(zero_x)
twos = len(two_x)
select_index = list(range(zeros))
select_index = list(combinations(select_index, 3))

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def bfs(y, x):

    queue = deque([])
    queue.append([y, x])

    while queue:
        y, x = queue.pop()
        for d in range(4):
            xx = dx[d] + x
            yy = dy[d] + y
            if 0 <= xx < M and 0 <= yy < N:
                if new_lab[yy][xx] == 0:
                    new_lab[yy][xx] = 2
                    queue.append([yy, xx])
answer = 0
for a, b, c in select_index:
    new_lab = copy.deepcopy(lab)
    new_lab[zero_y[a]][zero_x[a]] = 1
    new_lab[zero_y[b]][zero_x[b]] = 1
    new_lab[zero_y[c]][zero_x[c]] = 1
    for i in range(twos):
        bfs(two_y[i], two_x[i])

    safety = 0
    for i in range(N):
        for j in range(M):
            if new_lab[i][j] == 0: safety += 1

    if safety > answer : answer = safety

print(answer)