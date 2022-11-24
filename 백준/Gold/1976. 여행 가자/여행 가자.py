# N cities, N <= 200, M plans, M <= 1000
# YES or NO

from collections import deque
import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

graph = {}
for i in range(1, N + 1):
    graph[i] = [0] + list(map(int, sys.stdin.readline().split()))
plan = list(map(int, sys.stdin.readline().split()))

def bfs(g, start, dest):
    if start == dest: return True
    visited = [False] * (N + 1)
    visited[0] = True; visited[start] = True
    queue = deque()
    for city, road in enumerate(g[start]):
        if road == 1: queue.append(city)
    while queue:
        city = queue.popleft()
        if city == dest: return True
        if not visited[city]:
            for new_city, road in enumerate(g[city]):
                if road == 1: queue.append(new_city)
            visited[city] = True
    return False

is_available = True
cur = 0
for i in range(M):
    if i == 0: cur = plan[i]
    else:
        next = plan[i]
        if not bfs(graph, cur, next):
            print('NO')
            is_available = False
            break
        else:
            cur = next
if is_available: print('YES')