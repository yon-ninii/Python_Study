def solution(n, m):
    mini = min(n, m)
    maxi = max(n, m)
    g = 1
    c = 0
    for i in range(1, mini + 1):
        if n % i == 0 and m % i == 0 : g = i
    for i in range(mini, maxi ** 2, mini):
        if i % maxi == 0 : 
            c = i
            break
    return [g, c]