import sys
from itertools import permutations


N, M = map(int, input().strip().split())
l = [i for i in range(1, N + 1)]
p = list(permutations(l, M))

for i in p:
    for j in range(len(i)):
        print(i[j], end = ' ')
    print('')
