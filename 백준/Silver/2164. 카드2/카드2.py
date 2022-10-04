import sys
from collections import deque

N = int(sys.stdin.readline().strip())
card = deque(list(i for i in range(1, N + 1)))
def rotate(c):
    first = c.popleft()
    second = c.popleft()
    c.append(second)
    return c

for _ in range(N - 1):
    card = rotate(card)
ans = card.pop()
print(ans)