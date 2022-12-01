def solution(A,B):
    a = sorted(A)
    b = sorted(B)
    answer = 0
    for i in range(len(A)):
        answer += a[-1] * b[0]
        del a[-1]
        del b[0]
    return answer