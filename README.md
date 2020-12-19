# Binary Search Tree

## Implementation of a BST using Functional Programming

## Table of Contents

1. [Introduction](#introduction)
2. [List of Functions](#functions)
3. [Examples](#examples)
4. [Description of Functions](#description-of-functions)

## Introduction

This implementation of a binary search tree (BST) follows the Functional Programming Paradigm as it adheres to:
-   Immutability
-   Pure functions
-   Avoiding side-effects

It also allows for any data which can be ordered using a total order to be stored (not only numbers). This is done using a strict total order. If you want numbers to be stored by increasing order (like 1, 2, 3, 4, 5), use the total order "<" implemented by: lambda x, y : x < y

## Functions

The following functions are implemented:
-   BST(strict_total_order)
-   insert(tree, element)
-   remove(tree, element)
-   contains(tree, element)
-   size(tree)
-   is_empty(tree)
-   get_min(tree)
-   get_max(tree)
-   dump(tree) \*\*this is an impure function

## Examples

**Real Numbers Sorted on <**

Create a BST with elements 1 - 10 sorted by the strict total order "<"
```python
from random import shuffle
# create the list of elements to insert
elements_to_insert = [num for num in range(1, 11)]
shuffle(elements_to_insert) # ensures the tree is probabaly near minimal height

# create the BST
strict_total_order = lambda x, y : x < y
my_bst = BST(strict_total_order)
for element in elements_to_insert:
	my_bst = insert(my_bst, element)

# print the contents of the BST
dump(my_bst)

without_2 = remove(my_bst, 2)
dump(without_2)

print(is_empty(my_bst))

print(size(my_bst))

print(get_min(my_bst))
```

The output is:
```python
1 2 3 4 5 6 7 8 9 10
1 3 4 5 6 7 8 9 10
False
10
1
```


**Objects**

Using a BST to organize dogs age
```python
from functools import reduce

# Dog class
class Dog:
	def __init__(self, name, age):
		self.name = name
		self.age = age

dog1 = Dog("Brownie", 1)
dog2 = Dog("Jack", 8)
dog3 = Dog("Spark", 4)
dog4 = Dog("Ruby", 6)
dogs = [dog1, dog2, dog3, dog4]

strict_total_order = lambda dog1, dog2 : dog1.age < dog2.age
empty_bst = BST(strict_total_order)

dogs_bst = reduce(insert, dogs, empty_bst)

print(contains(dogs_bst, dog1))
print(contains(dogs_bst, Dog("Bear", 2)))
print(get_min(dogs_bst).name)
print(size(dogs_bst))
```

The output is:
```python
True
False
"Brownie"
4
```


## Description of Functions

**BST(strict_total_order)**
-   O(1) time
-   takes a strict total order
-   returns an empty BST with that total order <br> <br>

**insert(tree, element)**
-   O(h) time where h is the height of tree
-   takes a BST and an element
-   returns a BST with the elements of tree and element <br> <br>

**remove(tree, element)**
-   O(h) time where h is the height of tree
-   takes a non-empty BST which contains element and an element
-   returns a BST with the elements of tree except for element <br> <br>

**contains(tree, element)**
-   O(h) time where h is the height of tree
-   takes a BST and an element
-   returns true if element is in tree; false otherwise <br> <br>

**size(tree)**
-   O(n) time where n = size(tree)
-   takes a BST
-   returns the number of elements in tree <br> <br>

**is_empty(tree)**
-   O(1) time
-   takes a BST
-   returns true if tree if tree is an empty BST; false otherwise <br> <br>

**get_min(tree)**
-   O(h) time where h is the height of tree
-   takes a non-empty BST
-   returns the minimum element of tree <br> <br>

**get_max(tree)**
-   O(h) time where h is the height of tree
-   takes a non-empty BST
-   returns the maximum element of tree <br> <br>

**dump(tree)**
-   this is an impure function
-   O(n) time where n = size(tree)
-   takes a BST
-   prints the elements of tree
