import math

def solution(begin, end): # 1000000000 10000000
    answer = []
    for k in range(begin, end + 1):
        if k == 1: answer.append(0)
        else:
            for i in range(2, int(math.sqrt(k)) + 1):
                p = k // i
                if p > 10 ** 7: continue
                if k % i == 0:
                    answer.append(p)
                    break
            else: answer.append(1)
    return answer