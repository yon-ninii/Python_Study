import sys
from collections import defaultdict, deque
C = int(input().strip())
P = int(input().strip())
net = defaultdict(list)
for _ in range(P):
    a, b = map(int, sys.stdin.readline().strip().split())
    net[a].append(b)
    net[b].append(a)
def bfs(graph, root):
    need_visited = deque([root])
    visited = {}
    cnt = 0
    for k in graph.keys():
        visited[k] = 0
    while need_visited:
        node = need_visited.popleft()
        if visited[node] == 0:
            cnt += 1
            visited[node] = 1
            for a in graph[node]:
                need_visited.append(a)
    return cnt

print(bfs(net, 1) - 1)