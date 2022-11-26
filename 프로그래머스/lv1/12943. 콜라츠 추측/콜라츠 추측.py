def solution(num):
    def check(cnt, n):
        if n == 1 : return cnt
        elif cnt == 500 : return -1
        elif n % 2 == 0 : 
            n /= 2
            cnt = check(cnt + 1, n)
        else : 
            n = n * 3 + 1
            cnt = check(cnt + 1, n)
        return cnt
    return check(0, num)