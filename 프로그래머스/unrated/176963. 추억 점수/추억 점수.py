def solution(name, yearning, photo):
    score = dict()
    for i, n in enumerate(name):
        score[n] = yearning[i]
    
    answer = []
    
    for p in photo:
        summ = 0
        for person in p:
            if person not in name:
                continue
            summ += score[person]
        answer.append(summ)

    return answer