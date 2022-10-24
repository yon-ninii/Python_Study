def solution(n):
    three = ''
    while n > 0:
        if n % 3 == 0 :
            three = '3' + three
            n = n // 3 - 1
        else:
            three = str(n % 3) + three
            n = n // 3
    t = ['0', '1', '2', '4']
    answer = []
    for i in range(len(three)):
        answer.append(t[int(three[i])])
    return ''.join(answer)