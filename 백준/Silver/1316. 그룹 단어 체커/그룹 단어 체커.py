import sys

n = int(input())
string = []
for _ in range(n):
    string.append(sys.stdin.readline().strip())

answer = 0

for s in string:
    stack = []
    yes_flag = True
    for j in range(len(s)):
        if s[j] not in stack: stack.append(s[j])
        elif s[j] in stack and stack[-1] == s[j]: stack.append(s[j])
        elif s[j] in stack and stack[-1] != s[j]:
            yes_flag = False
            break
    if yes_flag: answer += 1

print(answer)
