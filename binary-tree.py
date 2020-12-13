# Binary tree implementation in Python

# total order is a strict total order
# Insert
# Remove
# Is Empty
# Size
# Contains

import math


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def p(self):
        print(f"value: {self.value}\nleft: {self.left}\nright: {self.right}")


class BinaryTree:
    def __init__(self, total_order):
        self.root = None
        self.to_strict = total_order
        self.to_equals = lambda a, b: (
            not self.to_strict(a, b)) and (not self.to_strict(b, a))

    # O(log n) time
    def insert(self, num):
        def helper(root):
            if root is None:
                root = Node(num)
                return root
            elif self.to_equals(root.value, num):
                return root
            elif self.to_strict(num, root.value):
                # insert left
                value = root.value
                left = helper(root.left)
                right = root.right
                return Node(value, left, right)
            else:
                value = root.value
                left = root.left
                right = helper(root.right)
                return Node(value, left, right)

        self.root = helper(self.root)

    # O(log n) time
    def remove(self, num):
        def remove_min(root):
            if root is None:
                return None
            elif root.left is None:
                return root.right
            else:
                value = root.value
                left = remove_min(root.left)
                right = root.right
                return Node(value, left, right)

        def get_min(root):
            if root is None:
                return None
            elif root.left is None:
                return root.value
            else:
                return get_min(root.left)

        def helper(root):
            if root is None:
                # root is empty
                # return None
                return None
            elif self.to_equals(num, root.value):
                # the root is the value to remove
                if root.left is None:
                    # the left is empty
                    # return right subtree
                    return root.right
                elif root.right is None:
                    # the right is empty
                    # return the left subtree
                    return root.left
                else:
                    # the left and right are both not empty
                    value = get_min(root.right)
                    left = root.left
                    right = remove_min(root.right)
                    return Node(value, left, right)
            elif self.to_strict(num, root.value):
                value = root.value
                left = helper(root.left)
                right = root.right
                return Node(value, left, right)
            elif self.to_strict(root.value, num):
                value = root.value
                left = root.left
                right = helper(root.right)
                return Node(value, left, right)

        self.root = helper(self.root)

    # O(log n) time
    def contains(self, num):
        def helper(root):
            if root is None:
                return False
            elif self.to_equals(root.value, num):
                return True
            elif self.to_strict(num, root.value):
                # search the left sutree
                return helper(root.left)
            else:
                return helper(root.right)
        return helper(self.root)

    def size(self):
        def helper(root):
            if root is None:
                return 0
            else:
                return 1 + helper(root.left) + helper(root.right)
        return helper(self.root)

    # O(1) time
    def is_empty(self):
        return self.root is None

    # O(log n) time
    def dump(self):
        def helper(root):
            if root is not None:
                helper(root.left)
                print(root.value)
                helper(root.right)
        helper(self.root)


a = BinaryTree(lambda a, b: a < b)
a.insert(10)
a.insert(20)
a.insert(30)
a.insert(1)


a.dump()
a.remove(10)
a.dump()
print(a.size())


b = BinaryTree(lambda a, b: math.abs(a) < math.abs(b))
print(b.is_empty())
