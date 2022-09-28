import sys
from collections import defaultdict, deque

N, M, root = map(int, input().strip().split())
graph = defaultdict(list)

for _ in range(M):
	a, b = map(int, sys.stdin.readline().strip().split())
	graph[a].append(b)
	graph[b].append(a)

for k in graph.keys():
	graph[k].sort()
def bfs(graph, root):
	need_visited = deque([root])
	visited = []
	result = []
	while need_visited:
		node = need_visited.popleft()
		if node not in visited:
			visited.append(node)
			need_visited += deque(graph[node])
			result.append(node)
	return result

def dfs(graph, root):
	need_visited = [root]
	visited = []
	result = []
	while need_visited:
		node = need_visited.pop()
		if node not in visited:
			visited.append(node)
			need_visited.extend(reversed(graph[node]))
			result.append(node)
	return result

b = bfs(graph, root)
d = dfs(graph, root)
for i in d:
	print(i, end=' ')
print('')
for i in b:
	print(i, end=' ')
