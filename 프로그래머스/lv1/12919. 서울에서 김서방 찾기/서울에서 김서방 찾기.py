def solution(seoul):
    x = 0
    for i in range(len(seoul)):
        if seoul[i] == 'Kim':
            x = i
            break
    return f'김서방은 {x}에 있다'