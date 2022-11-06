def solution(s):
    l = sorted(s)
    string = ''
    for i in l[::-1]:
        string += i
    return string