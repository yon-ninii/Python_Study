import sys
from collections import defaultdict, deque
N = int(input().strip())
tree = defaultdict(list)
for _ in range(N - 1):
    a, b = map(int, sys.stdin.readline().strip().split())
    tree[a].append(b)
    tree[b].append(a)
def bfs(graph, root):
    need_visited = deque([(root, 0)])
    visited = {}
    for k in graph.keys():
        visited[k] = 0
    while need_visited:
        node, p = need_visited.popleft()
        if visited[node] == 0:
            visited[node] = p
            for a in graph[node]:
                need_visited.append((a, node))
    return visited

dic = bfs(tree, 1)
for i in range(2, N + 1):
    print(dic[i])