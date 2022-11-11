def solution(n):
    string = '수박'
    if n == 1 : return '수'
    elif n % 2 == 1 : return string * (n // 2) + '수'
    else : return string * (n // 2)