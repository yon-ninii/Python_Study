import sys

T = int(sys.stdin.readline())

M, N, cab, X, Y = [], [], [], [], []

land = []

for i in range(T):
    arr = []
    m, n, num = map(int, sys.stdin.readline().split())
    M.append(m)
    N.append(n)
    cab.append(num)
    for _ in range(n):
        arr.append([0] * m)
    for _ in range(num):
        x, y = map(int, sys.stdin.readline().split())
        X.append(x)
        Y.append(y)
        arr[y][x] = 1
    land.append(arr)

def print_pretty(l): # 5x5로 출력해주는 함수
    for line in l:
        print(line)

print_pretty(land[0])

def check_near(w, h, cabbage, a, b):
    near = []
    for _ in range(h):
        near.append([0] * w)
    for i in range(cabbage - 1):
        for j in range(i + 1, cabbage):
            if b[i] == b[j]:
                if a[i] == a[j] + 1:
                    near[b[i]][a[i]] += 1
            if a[i] == a[j]:
                if b[i] == b[j] + 1:
                    near[b[i]][a[i]] += 1
    for i in range(cabbage - 1, 0, -1):
        for j in range(i - 1, -1, -1):
            if b[i] == b[j] and a[i] == a[j] - 1:
                near[b[i]][a[i]] += 1
            if a[i] == a[j] and b[i] == b[j] - 1:
                near[b[i]][a[i]] += 1
    return near

for i in range(T):
    result = check_near(M[i], N[i], cab[i], X[i * cab[i - 1]:i * cab[i - 1] + cab[i]], Y[i * cab[i - 1]:i * cab[i - 1] + cab[i]])
    print_pretty(result)