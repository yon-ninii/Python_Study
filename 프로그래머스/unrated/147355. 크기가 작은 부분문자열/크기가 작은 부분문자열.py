def solution(t, p):
    n, m = len(t), len(p)
    num_partial = n - m + 1
    answer = 0
    for k in range(num_partial):
        if int(t[k : k + m]) <= int(p):
            print(int(t[k : k + m]))
            answer += 1
    return answer