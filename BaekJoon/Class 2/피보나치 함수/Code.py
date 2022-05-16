import sys

num = int(sys.stdin.readline())
N_list = []
for _ in range(num):
    N_list.append(int(sys.stdin.readline().strip()))

def fibo(n):
    i = 2
    ones = [0, 1, 1]
    zeros = [1, 0, 1]

    if n == 0: return ones[n], zeros[n]
    elif n == 1: return ones[n], zeros[n]
    elif n == 2: return ones[n], zeros[n]

    while i < n:
        ones.append(ones[i] + ones[i - 1])
        zeros.append(zeros[i] + zeros[i - 1])
        i += 1

    return ones[n], zeros[n]

for i in range(num):
    one, zero = fibo(N_list[i])
    print(zero, one)