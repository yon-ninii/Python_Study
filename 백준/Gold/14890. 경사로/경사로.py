from copy import deepcopy

N, L = map(int, input().split())

roads = [list(map(int, input().split())) for _ in range(N)]

def valid_road(road):
    stack = deepcopy(road)
    num = 1
    prev = stack.pop()
    is_down = False
    while stack:
        cur = stack.pop()
        if is_down:
            if prev != cur: return False
            elif prev == cur:
                num += 1
                if num >= L:
                    is_down = False
                    num = 0
        elif prev == cur: num += 1 # 같은 높이일 때
        elif prev == cur - 1: # 한칸 올라 갔을 때
            if num >= L:
                prev = cur
                num = 1
            else: return False
        elif prev == cur + 1: # 한칸 내려 갔을 때
            is_down = True
            num = 1
            if num >= L:
                is_down = False
                num = 0
            prev = cur
        else: return False
    if is_down: return False
    return True

answer = 0

for i in range(N):
    if valid_road(roads[i][:]):
        answer += 1
    col_list = []
    for j in range(N):
        col_list.append(roads[j][i])
    if valid_road(col_list):
        answer += 1

print(answer)