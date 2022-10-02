import sys

N = int(sys.stdin.readline())
P = []

for _ in range(N):
    P.append(list(map(int, sys.stdin.readline().split())))

result = [0, 0, 0]

def paper_check(paper, num, result, a, b):
    answer = paper[a][b]
    new_num = num // 3
    if num == 1 : result[answer] += 1
    else:
        paper_flag = True
        for i in range(a, a + num):
            for j in range(b, b + num):
                if paper[i][j] != answer:
                    paper_flag = False
                    for x in range(3):
                        for y in range(3):
                            paper_check(paper, new_num, result, a + x * new_num, b + y * new_num)
                    break
            if paper_flag == False: break
        if paper_flag:
            result[paper[a][b]] += 1

paper_check(P, N, result, 0, 0)

print(result[-1])
print(result[0])
print(result[1])