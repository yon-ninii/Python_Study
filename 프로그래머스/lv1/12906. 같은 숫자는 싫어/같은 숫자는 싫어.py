def solution(arr):
    pre, i = -1, 0
    answer = []
    for _ in range(len(arr)):
        if pre == arr[i] : i += 1
        else : 
            pre = arr[i]
            answer.append(pre)
            i += 1
    return answer