def solution(n):
    l = [i for i in range(1, n)]
    cnt = 1
    for i in range(len(l)):
        j = i
        t = l[i]
        while t <= n:
            if t == n: 
                cnt += 1
                break
            if j == n - 2: break
            j += 1
            t += l[j]
    return cnt