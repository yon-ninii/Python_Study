def solution(s):
    l = list(map(int, s.split()))
    a = min(l)
    b = max(l)
    return f'{a} {b}'