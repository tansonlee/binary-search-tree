# *****************************************************************************************
# ***** Binary tree implementation in Python **********************************************
# *****************************************************************************************

#### total order is a strict total order

# BST(strict_total_order) : O(1) time
# 	function -> BST
# 	returns and empty BST with the strict total order

# insert(tree, num) : O(log(n)) where n = size(tree)
# 	BST -> BST
# 	returns a BST with all the elements of tree and num

# remove(tree, num) : O(log(n)) where n = size(tree)
# 	BST -> BST
# 	returns a BST with all the elements of tree except num

# is_empty(tree) : O(1)
# 	BST -> boolean
# 	returns true if tree is an empty BST; false otherwise

# size(tree) : O(n) where n = size(tree)
# 	BST -> integer
# 	returns the number of nodes in tree

# contains(tree, num) : O(log(n)) where n = size(tree)
# 	BST -> boolean
# 	returns true if num is an element of tree; false otherwise

# dump(tree) : O(log(n)) where n = size(tree)
# 	BST -> void
# 	prints the elements of tree

# get_min(tree) : O(log(n)) where n = size(tree)
# 	BST -> <type of elements in tree>
# 	returns the minimum element in tree

# get_max(tree) : O(log(n)) where n = size(tree)
# 	BST -> <type of elements in tree>
# 	returns the maximum element in tree

import math
import random

class Node:
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right

	def p(self):
		print(f"value: {self.value}\nleft: {self.left}\nright: {self.right}")

class BST:
	def __init__(self, total_order, root=None):
		self.to_strict = total_order
		self.root = root


def dump(tree):
	root = tree.root
	to_strict = tree.to_strict
	if root is not None:
		dump(BST(to_strict, root.left))
		print(root.value, end=" ")
		dump(BST(to_strict, root.right))

def insert(tree, num):
	root = tree.root
	to_strict = tree.to_strict
	to_equals = lambda x, y : (not to_strict(x, y)) and (not to_strict(y, x))

	def helper(root, num):
		if root is None:
			new_root = Node(num)
			return new_root
		
		elif to_equals(num, root.value):
			return root
		
		elif to_strict(num, root.value):
			# insert into left subtree
			value = root.value
			left = helper(root.left, num)
			right = root.right
			return Node(value, left, right)
		
		elif to_strict(root.value, num):
			# insert into right subtree
			value = root.value
			left = root.left
			right = helper(root.right, num)
			return Node(value, left, right)

		else:
			# used for debugging
			return "Error"
		
	new_root = helper(root, num)
	return BST(to_strict, new_root)

def remove(tree, num):
	root = tree.root
	to_strict = tree.to_strict
	to_equals = lambda x, y : (not to_strict(x, y)) and (not to_strict(y, x))

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
	
	def remove_max(root):
		if root is None:
			return None
		elif root.right is None:
			return root.left
		else:
			value = root.value
			left = root.left
			right = remove_max(root.right)
			return Node(value, left, right)

	def helper(root, num):
		if root is None:
			# root is empty
			return None
		elif to_equals(num, root.value):
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
				r = random.randint(0, 1)
				if r == 0:
					value = get_min(BST(to_strict, root.right))
					left = root.left
					right = remove_min(root.right)
					return Node(value, left, right)
				elif r == 1:
					value = get_max(BST(to_strict, root.left))
					left = remove_max(root.left)
					right = root.right
					return Node(value, left, right)
		elif to_strict(num, root.value):
			value = root.value
			left = helper(root.left, num)
			right = root.right
			return Node(value, left, right)
		elif to_strict(root.value, num):
			value = root.value
			left = root.left
			right = helper(root.right, num)
			return Node(value, left, right)	

	new_root = helper(root, num)
	return BST(to_strict, new_root)

def get_min(tree):
	root = tree.root

	def helper(root):
		if root is None:
			return None
		elif root.left is None:
			return root.value
		else:
			return helper(root.left)

	return helper(root)

def get_max(tree):
	root = tree.root

	def helper(root):
		if root is None:
			return None
		elif root.right is None:
			return root.value
		else:
			return helper(root.right)

	return helper(root)
	
def contains(tree, num):
	root = tree.root
	to_strict = tree.to_strict
	to_equals = lambda x, y : (not to_strict(x, y)) and (not to_strict(y, x))

	def helper(root, num):
		if root is None:
			return False
		elif to_equals(root.value, num):
			return True
		elif to_strict(num, root.value):
			# search the left sutree
			return helper(root.left, num)
		elif to_strict(root.value, num):
			return helper(root.right, num)

	return helper(root, num)

def size(tree):
	root = tree.root

	def helper(root):
		if root is None:
			return 0
		else:
			return 1 + helper(root.left) + helper(root.right)
	
	return helper(root)

def is_empty(tree):
	root = tree.root
	return root is None
