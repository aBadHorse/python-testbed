

class Node():
    '''Object representing a binary node for a tree data structure'''
    def __init__(self, value):
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
