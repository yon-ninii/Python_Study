def solution(s):
    bracket = ['(', ')']
    b1 = 0
    #if s[0] == bracket[1]: return False
    #elif s[1] == bracket[0]: return False
    i = 0
    while i < len(s) and b1 >= 0:
        if s[i] == bracket[0] : b1 += 1
        elif s[i] == bracket[1] : b1 -= 1
        i += 1
    return b1 == 0