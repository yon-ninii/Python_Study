# 기본 제공코드는 임의 수정해도 관계 없습니다. 단, 입출력 포맷 주의
# 아래 표준 입출력 예제 필요시 참고하세요.

# 표준 입력 예제
'''
a = int(input())                        정수형 변수 1개 입력 받는 예제
b, c = map(int, input().split())        정수형 변수 2개 입력 받는 예제 
d = float(input())                      실수형 변수 1개 입력 받는 예제
e, f, g = map(float, input().split())   실수형 변수 3개 입력 받는 예제
h = input()                             문자열 변수 1개 입력 받는 예제
'''

# 표준 출력 예제
'''
a, b = 6, 3
c, d, e = 1.0, 2.5, 3.4
f = "ABC"
print(a)                                정수형 변수 1개 출력하는 예제
print(b, end = " ")                     줄바꿈 하지 않고 정수형 변수와 공백을 출력하는 예제
print(c, d, e)                          실수형 변수 3개 출력하는 예제
print(f)                                문자열 1개 출력하는 예제
'''

#import sys


'''
      아래의 구문은 input.txt 를 read only 형식으로 연 후,
      앞으로 표준 입력(키보드) 대신 input.txt 파일로부터 읽어오겠다는 의미의 코드입니다.
      여러분이 작성한 코드를 테스트 할 때, 편의를 위해서 input.txt에 입력을 저장한 후,
      아래 구문을 이용하면 이후 입력을 수행할 때 표준 입력 대신 파일로부터 입력을 받아올 수 있습니다.

      따라서 테스트를 수행할 때에는 아래 주석을 지우고 이 구문을 사용하셔도 좋습니다.
      아래 구문을 사용하기 위해서는 import sys가 필요합니다.

      단, 채점을 위해 코드를 제출하실 때에는 반드시 아래 구문을 지우거나 주석 처리 하셔야 합니다.
'''
#sys.stdin = open("input.txt", "r")
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
 
def deepcopy(lst):
    new_lst = []
    for y in range(len(lst)):
        temp = []
        for x in range(len(lst[y])):
            temp.append(lst[y][x])
        new_lst.append(temp)
    return new_lst
 
def erase_bricks(y, x, cur_bricks):
    Q = [(y, x, cur_bricks[y][x])]
    cur_bricks[y][x] = 0
 
    erased_bricks = 1
    while Q:
        cur_y, cur_x, cur_power = Q.pop(0)
 
        for p in range(1, cur_power):
            for d in range(4):
                new_y, new_x = cur_y + p * dy[d], cur_x + p * dx[d]
                if -1 < new_y < H and -1 < new_x < W and cur_bricks[new_y][new_x] != 0:
                    if cur_bricks[new_y][new_x] != 1:
                        Q.append((new_y, new_x, cur_bricks[new_y][new_x]))
                    erased_bricks += 1
                    cur_bricks[new_y][new_x] = 0
 
    return erased_bricks
 
def sort_bricks(cur_bricks):
    for x in range(W):
        cur_w_bricks = []
        for y in range(H - 1, -1, -1):
            if cur_bricks[y][x] != 0:
                cur_w_bricks.append(cur_bricks[y][x])
                cur_bricks[y][x] = 0
 
        for h in range(len(cur_w_bricks)):
             cur_bricks[H - 1 - h][x] = cur_w_bricks[h]
 
 
def dfs(result, k, bricks):
    global max_result
    if k == N:
        if max_result < result:
            max_result = result
        return
 
    for w in range(W):
        cur_bricks = deepcopy(bricks)
        cur_h = 0
 
        while cur_h < H and not cur_bricks[cur_h][w]:
            cur_h += 1
 
        num_erase = 0
        if cur_h < H:
            num_erase = erase_bricks(cur_h, w, cur_bricks)
            sort_bricks(cur_bricks)
        dfs(result + num_erase, k + 1, cur_bricks)
 
 
 
for tc in range(int(input())):
    N, W, H = map(int, input().split())
 
    origin_bricks = [list(map(int, input().split())) for _ in range(H)]
    num_all_bricks = 0
    for y in range(H):
        for x in range(W):
            if origin_bricks[y][x] != 0:
                num_all_bricks += 1
 
    max_result = 0
    dfs(0, 0, origin_bricks)
 
    print('#{} {}'.format(tc + 1, num_all_bricks - max_result))
    # ///////////////////////////////////////////////////////////////////////////////////
