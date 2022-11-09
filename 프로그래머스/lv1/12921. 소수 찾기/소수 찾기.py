def solution(n):
    if n == 2 : return 1
    l_not = []
    root = int(n ** 0.5) + 1
    for i in range(2, root):
        a = 2
        while i * a <= n:
            l_not.append(i * a)
            a += 1
    return n - 1 - len(set(l_not))