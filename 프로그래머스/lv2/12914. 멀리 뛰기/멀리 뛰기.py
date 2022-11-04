def solution(n):
    if n == 0: return 0
    elif n == 1: return 1
    elif n == 2: return 2
    a, b, answer = 1, 1, 2
    for _ in range(n - 2):
        a = b
        b = answer
        answer = a + b
    return answer % 1234567