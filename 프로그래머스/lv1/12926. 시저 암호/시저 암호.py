def solution(s, n):
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] 
    answer = []
    for i in range(len(s)):
        if s[i] == ' ': answer.append(' ')
        elif s[i] not in alpha:
            answer.append(alpha[(alpha.index(s[i].lower()) + n) % 26].upper())
        else:
            answer.append(alpha[(alpha.index(s[i]) + n) % 26])

    return ''.join(answer)