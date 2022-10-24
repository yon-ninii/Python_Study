def solution(n): 
    a, b, answer = 1, 2, 0
    if n == 1: return 1
    elif n == 2: return 2
    for _ in range(n - 2):
        answer = (a + b) % 1000000007
        a = b
        b = answer
    return answer