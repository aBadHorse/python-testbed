from objects import Node
from collections import deque

node1 = Node(1)
node4 = Node(4)
node3 = Node(3)
node3.set_left(node1)
node3.set_right(node4)
node6 = Node(6)
node9 = Node(9)
node8 = Node(8)
node8.set_left(node6)
node8.set_right(node9)
node5 = Node(5)
node5.set_left(node3)
node5.set_right(node8)

# node5 is root of a complete balanced binary search tree
# bfs() should return:
# 5
# 38
# 1469

def bfs(root):
    clevel = 1
    root.set_level(1)
    queue = deque([root])
    while(len(queue) > 0):
        node = queue.popleft()
        if node.level != clevel:
            clevel += 1
            print()
        print(node.value, end=' ')
        if node.has_right():
            right = node.right
            right.set_level(node.level + 1)
            queue.append(right)
        if node.has_left():
            left = node.left
            left.set_level(node.level + 1)
            queue.append(left)

def dfs(node):
    if node.has_left():
        dfs(node.left)
    if node.has_right():
        dfs(node.right)
    print(node.value, end=' ')

def search(node, val):
    if val == node.value:
        return True
    elif val < node.value and node.has_left():
        return search(node.left, val)
    elif val > node.value and node.has_right():
        return search(node.right, val)
    else:
        return False

print('breadth first search of a binary tree')
bfs(node5)
print('\n\ndepth first search of a binary tree')
dfs(node5)
print('\n\nsearching binary tree')
for i in range(10):
    print(i, search(node5, i))
