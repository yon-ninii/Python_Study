from collections import deque

def solution(maps):
    m = len(maps)
    n = len(maps[0])
    def is_map(y, x):
        return y >= 0 and x >= 0 and y < m and x < n
    def bfs(graph, cnt):
        need_visited = deque([(0, 0, cnt)])
        while need_visited:
            y, x, c = need_visited.popleft()
            if not graph[y][x]: continue
            c += 1
            if y == m - 1 and x== n - 1: return c
            graph[y][x] = 0
            ay, ax, by, bx, cy, cx, dy, dx = y + 1, x, y - 1, x, y, x + 1, y, x - 1
            if is_map(ay, ax): need_visited.append((ay, ax, c))
            if is_map(by, bx): need_visited.append((by, bx, c))
            if is_map(cy, cx): need_visited.append((cy, cx, c))
            if is_map(dy, dx): need_visited.append((dy, dx, c))
        return -1
    return bfs(maps, 0)