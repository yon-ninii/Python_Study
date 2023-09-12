import sys
from collections import deque, defaultdict

def Input_Data():
    R, C = map(int,readl().split())
    art, water = (0, 0), []
    map_forest = []
    for i in range(R):
        map_forest.append(list(readl()[:-1]))
        for j, f in enumerate(map_forest[-1]):
            if f == 'S': art = (i, j)
            elif f == '*': water.append((i, j))
    return R, C, map_forest, art, water


readl = sys.stdin.readline
sol = 0
# 입력받는 부분
R, C, map_forest, art, water = Input_Data()

# 여기서부터 작성 
min_move = 0

visited = defaultdict(int)

# 작성하는 부분
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# 데크 초기화 및 시작 인덱스 입력
moves = deque()
cur_move = 0
moves.append((art[0], art[1], cur_move))
visited[art] = 1

flood = deque()
for wx, wy in water:
    flood.append((wx, wy))

def is_valid(nx, ny):
    return (nx >= 0 and nx < R) and (ny >= 0 and ny < C)

while moves:
    x, y, move = moves.popleft()

    if map_forest[x][y] == 'D': 
        min_move = move
        break

    if move != cur_move:
        cur_move = move
        for _ in range(len(flood)):
            wx, wy = flood.popleft()
            for i in range(4):
                nwx = wx + dx[i]
                nwy = wy + dy[i]
                if not is_valid(nwx, nwy) or map_forest[nwx][nwy] == '*': continue
                if map_forest[nwx][nwy] == 'X' or map_forest[nwx][nwy] == 'D': continue
                flood.append((nwx, nwy))
                map_forest[nwx][nwy] = '*'
    if map_forest[x][y] == '*': continue
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if not is_valid(nx, ny) or visited[(nx, ny)]: continue
        if map_forest[nx][ny] == 'X' or map_forest[nx][ny] == '*': continue
        moves.append((nx, ny, move + 1))
        visited[(nx, ny)] = 1

if min_move == 0: sol = 'KAKTUS'
else: sol = min_move

# 출력하는 부분
print(sol)