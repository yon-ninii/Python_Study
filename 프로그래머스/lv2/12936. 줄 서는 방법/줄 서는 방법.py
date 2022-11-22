import math
def solution(n, k):
    if n == 1:
        return [1]
    ans = []
    li = [x for x in range(1, n + 1)]
    for i in range(n - 1, 0, -1):
        i_fac = math.factorial(i)
        c = int(k / i_fac)
        r = k % i_fac
        if r != 0:
            c += 1
        ans.append(li[c - 1])
        li.remove(li[c - 1])
        k = r
        if k == 0:
            li.reverse()
            ans += li
            break
    return ans