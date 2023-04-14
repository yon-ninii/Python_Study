def binary_trans(num):
    result = 0
    strs = 0
    for n in num:
        if n == '0': 
            result += 1
        else:
            strs += 1
    return result, format(strs, 'b')

def solution(s):
    zeros, gen = 0, 0
    while True:
        if s == '1': break
        tmp, s = binary_trans(s)
        gen += 1
        zeros += tmp
    return [gen, zeros]