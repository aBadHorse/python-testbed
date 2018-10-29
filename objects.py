from random import random
from math import floor
from decorators import profile_me


class Node:
    def __init__(self, value) -> object:
        """Object representing a binary node for a tree data structure
        
            :rtype: object
        """
        self.value = value
        self.left = None
        self.right = None
        self.level = None

    def set_left(self, obj):
        self.left = obj

    def set_right(self, obj):
        self.right = obj

    def set_level(self, l):
        self.level = l

    def get_level(self):
        return self.level

    def has_left(self):
        return self.left is not None

    def has_right(self):
        return self.right is not None


class Tree:
    def __init__(self, num_values, use_generator: bool) -> object:
        """Object representing a binary tree"""
        self.num_values = num_values
        self.root = None
        if use_generator:
            self.generate_tree()
        else:
            self.build_tree()

    @profile_me
    def generate_tree(self):
        for value in self.values():
            if self.root is None:
                self.root = Node(value)
            else:
                self.insert(self.root, value)

    @profile_me
    def build_tree(self):
        for value in [floor(random()*1000) for value in range(self.num_values)]:
            if self.root is None:
                self.root = Node(value)
            else:
                self.insert(self.root, value)

    def insert(self, root: Node, value: int):
        if value < root.value:
            if root.has_left():
                self.insert(root.left, value)
            else:
                root.left = Node(value)
        elif value > root.value:
            if root.has_right():
                self.insert(root.right, value)
            else:
                root.right = Node(value)

    def values(self):
        for value in range(self.num_values):
            yield floor(random()*1000)


