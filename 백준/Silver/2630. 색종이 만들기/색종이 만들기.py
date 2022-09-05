import sys
from collections import Counter

N = int(sys.stdin.readline().strip())
paper = []
for _ in range(N):
    p = list(map(int, sys.stdin.readline().strip().split()))
    paper.append(p)

def sum_list(l):
    result = 0
    for i in l:
        result += sum(i)
    return result
def tear(paper, n):
    a = n // 2
    s = sum_list(paper)
    if n == 1 and s == 0:
        return [1, 0]
    elif n == 1 and s == 1:
        return [0, 1]
    if s == n ** 2:
        return [0, 1]
    elif s == 0:
        return [1, 0]
    p1, p2, p3, p4 = [], [], [], []
    for i in range(n):
        if i < a:
            p1.append(paper[i][:a])
            p2.append(paper[i][a:])
        else:
            p3.append(paper[i][:a])
            p4.append(paper[i][a:])
    #t1, t2, t3, t4 =
    return tear(p1, a) + tear(p2, a) + tear(p3, a) + tear(p4, a)

l = list(tear(paper, N))
answer1, answer2 = 0, 0
for i in range(len(l)):
    if i % 2 == 0: answer1 += l[i]
    else: answer2 += l[i]
print(answer1, answer2)