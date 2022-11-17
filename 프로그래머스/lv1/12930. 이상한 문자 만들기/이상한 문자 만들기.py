def solution(s):
    answer = ''
    i, j = 0, 0
    while i < len(s):
        word = True
        if s[i] == ' ': 
            answer += ' '
            word = False
        elif j % 2 == 0 : 
            answer += s[i].upper()
            j += 1
        elif j % 2 == 1 :
            answer += s[i].lower()
            j += 1
        if not word: j = 0
        i += 1
    return answer