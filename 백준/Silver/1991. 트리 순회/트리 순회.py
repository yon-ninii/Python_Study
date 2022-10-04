import sys
from collections import defaultdict, deque

N = int(input().strip())
tree = defaultdict(list)

for _ in range(N):
    a, b, c = sys.stdin.readline().strip().split()
    tree[a].append(b)
    tree[a].append(c)

def preorder(t, node):
    print(node, end='')
    if t[node][0] != '.':
        preorder(t, t[node][0])
    if t[node][1] != '.':
        preorder(t, t[node][1])
    return

def inorder(t, node):
    if t[node][0] != '.':
        inorder(t, t[node][0])
    print(node, end='')
    if t[node][1] != '.':
        inorder(t, t[node][1])

    return

def postorder(t, node):
    if t[node][0] != '.':
        postorder(t, t[node][0])
    if t[node][1] != '.':
        postorder(t, t[node][1])
    print(node, end='')
    return

preorder(tree, 'A')
print('')
inorder(tree, 'A')
print('')
postorder(tree, 'A')
