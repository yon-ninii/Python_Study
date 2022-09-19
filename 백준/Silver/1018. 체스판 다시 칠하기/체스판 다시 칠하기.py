import sys

def num_chess_1(x, y, CB):
    num = 0
    ans1 = ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']
    ans2 = ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']
    
    for j in range(y, y + 8):
        for i in range(x, x + 8):
            if ((j - y) % 2) == 0:
                if CB[j][i] != ans1[i - x]:
                    num += 1
            if ((j - y) % 2) == 1:
                if CB[j][i] != ans2[i - x]:
                    num += 1
                
    return num

def num_chess_2(x, y, CB):
    num = 0
    ans1 = ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']
    ans2 = ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']
    
    for j in range(y, y + 8):
        for i in range(x, x + 8):
            if ((j - y) % 2) == 0:
                if CB[j][i] != ans1[i - x]:
                    num += 1
            if ((j - y) % 2) == 1:
                if CB[j][i] != ans2[i - x]:
                    num += 1
                
    return num


H, W = map(int, sys.stdin.readline().split())
CB = []

for _ in range(H):
    CB.append(list(sys.stdin.readline().strip()))

result = []
for y in range(H - 7):
    for x in range(W - 7):
        result.append(num_chess_1(x, y, CB))
        result.append(num_chess_2(x, y, CB))
        
print(min(result))