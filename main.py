from objects import Node, Tree
from collections import deque
from decorators import profile_me, delay_me
import gc

gc.disable()

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


@profile_me
def bft_exec(root):
    bft(root)


def bft(root):
    """Breadth first traversal of a binary tree"""
    clevel = 1
    root.set_level(1)
    queue = deque([root])
    while len(queue) > 0:
        node = queue.popleft()
        if node.level != clevel:
            clevel += 1
            print()
        print(node.value, end=' ')
        if node.has_left():
            left = node.left
            left.set_level(node.level + 1)
            queue.append(left)
        if node.has_right():
            right = node.right
            right.set_level(node.level + 1)
            queue.append(right)


@profile_me
def dft_exec(node):
    dft(node)


def dft(node) -> None:
    """Depth first traversal of a binary tree"""
    if node.has_right():
        dft(node.right)
    if node.has_left():
        dft(node.left)
    print(node.value, end=' ')


@delay_me(delay=.1)
# @profile_me
def search_exec(node, val):
    return search(node, val)


def search(node, val) -> bool:
    """Perform a search on a binary tree
    
        :rtype: bool
    """
    if val == node.value:
        return True
    elif val < node.value and node.has_left():
        return search(node.left, val)
    elif val > node.value and node.has_right():
        return search(node.right, val)
    else:
        return False

# node5 is root of a complete balanced binary search tree
# bfs() should return:
# 5
# 38
# 1469
print('breadth first traversal of a binary tree')
bft_exec(node5)

# dft() should return:
# 5
# 38
# 1469
# print('\n\ndepth first traversal of a binary tree')
# dft(node5)
# print('\n\nsearching binary tree')
# for i in range(10):
#     print(i, search(node5, i))

num_values = 100_000

tree = Tree(num_values, False)
tree = Tree(num_values, True)

bft_exec(tree.root)
dft_exec(tree.root)
for i in range(10):
    if not search_exec(tree.root, i):
        print(f'{i} not found')
    else:
        print(f'{i} found')

gc.collect()


