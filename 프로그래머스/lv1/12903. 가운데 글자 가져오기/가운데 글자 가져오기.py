def solution(s):
    is_odd = False
    if len(s) % 2 == 1 : is_odd = True
    if is_odd: 
        return s[len(s)//2]
    else: 
        return s[len(s)//2 - 1] + s[len(s)//2]