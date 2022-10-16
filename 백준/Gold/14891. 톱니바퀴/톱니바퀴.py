import sys
from collections import deque
from copy import deepcopy


w1 = list(map(int, list(sys.stdin.readline().strip())))
w2 = list(map(int, list(sys.stdin.readline().strip())))
w3 = list(map(int, list(sys.stdin.readline().strip())))
w4 = list(map(int, list(sys.stdin.readline().strip())))

K = int(sys.stdin.readline())

rotations = []
for _ in range(K):
    num, direction = map(int, sys.stdin.readline().split())
    rotations.append((num, direction))

w1 = deque(w1)
w2 = deque(w2)
w3 = deque(w3)
w4 = deque(w4)

def rotate(dir, wheel):
    if dir == 1:
        ten = wheel.pop()
        wheel.appendleft(ten)
    elif dir == -1:
        one = wheel.popleft()
        wheel.append(one)
    return wheel

def rot_func(dir, num, w1, w2, w3, w4):
    new_w1, new_w2, new_w3, new_w4 = deepcopy(w1), deepcopy(w2), deepcopy(w3), deepcopy(w4)
    w1_right = w1[2]
    w2_left = w2[-2]
    w2_right = w2[2]
    w3_left = w3[-2]
    w3_right = w3[2]
    w4_left = w4[-2]
    w1_w2 = (w1_right != w2_left)
    w2_w3 = (w2_right != w3_left)
    w3_w4 = (w3_right != w4_left)
    if num == 1:
        new_w1 = rotate(dir, w1)
        if w1_w2:
            new_w2 = rotate(dir * (-1), w2)
            if w2_w3:
                new_w3 = rotate(dir, w3)
                if w3_w4: new_w4 = rotate(dir * (-1), w4)
    elif num == 2:
        new_w2 = rotate(dir, w2)
        if w1_w2: new_w1 = rotate(dir * (-1), w1)
        if w2_w3:
            new_w3 = rotate(dir * (-1), w3)
            if w3_w4: new_w4 = rotate(dir, w4)
    elif num == 3:
        new_w3 = rotate(dir, w3)
        if w3_w4: new_w4 = rotate(dir * (-1), w4)
        if w2_w3:
            new_w2 = rotate(dir * (-1), w2)
            if w1_w2: new_w1 = rotate(dir, w1)
    elif num == 4:
        new_w4 = rotate(dir, w4)
        if w3_w4:
            new_w3 = rotate(dir * (-1), w3)
            if w2_w3:
                new_w2 = rotate(dir, w2)
                if w1_w2: new_w1 = rotate(dir * (-1), w1)

    return new_w1, new_w2, new_w3, new_w4

for num, direction in rotations:
    w1, w2, w3, w4 = rot_func(direction, num, w1, w2, w3, w4)

print(w1[0] + w2[0] * 2 + w3[0] * 4 + w4[0] * 8)