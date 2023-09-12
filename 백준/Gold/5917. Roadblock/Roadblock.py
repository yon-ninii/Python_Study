import sys
from collections import deque, defaultdict
from math import inf as INF

def Input_Data():
    readl = sys.stdin.readline
    N, M = map(int, readl().split())
    edges = [list(map(int, readl().split())) for _ in range(M)]
    return N, M, edges
    
sol = -1

# 입력받는 부분
N, M, edges = Input_Data()

# 여기서부터 작성
graph = defaultdict(dict)
for info in edges:
    if info[1] not in graph[info[0]].keys():
        graph[info[0]][info[1]] = []
        graph[info[1]][info[0]] = []
        graph[info[0]][info[1]].append(info[2])
        graph[info[1]][info[0]].append(info[2])
    else:
        graph[info[0]][info[1]].append(info[2])
        graph[info[1]][info[0]].append(info[2])

def bfs():
    cnt_field = [(INF,) for _ in range(N + 1)]
    cnt_field[1] = (0, -1)

    queue = deque()
    queue.append((1, 0))

    while queue:
        field, d = queue.popleft()
        if d > cnt_field[field][0]: continue
        for k in graph[field].keys():
            cost = min(graph[field][k])
            if d + cost >= cnt_field[k][0]: continue
            queue.append((k, d + cost))
            cnt_field[k] = (d + cost, field)
    
    return cnt_field

cnt_field = bfs()
first_min = cnt_field[-1][0]

paths = []
idx = -1
while True:
    if cnt_field[idx][1] == 1: break
    paths.append(cnt_field[idx][1])
    idx = cnt_field[idx][1]
paths = [1] + paths[::-1] + [N]

prev = 1
second_min = 0
for i in range(1, len(paths)):
    temp_idx = graph[prev][paths[i]].index(min(graph[prev][paths[i]]))
    temp_val = graph[prev][paths[i]][temp_idx]
    graph[prev][paths[i]][temp_idx] *= 2
    temp_min = bfs()[-1][0]
    if temp_min > second_min: second_min = temp_min
    graph[prev][paths[i]][temp_idx] = temp_val
    prev = paths[i]

sol = second_min - first_min

# 출력하는 부분
print(sol)