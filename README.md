# Binary Search Tree

## Implementation of a binary search tree in Python using Functional Programming

This implementation of a binary search tree (BST) follows the Functional Programming Paradigm as it adheres to:

-   Immutability
-   Pure functions
-   Avoiding side-effects

It also allows for any data which can be ordered using a total order to be stored (not only numbers). This is done using a strict total order. If you want numbers to be stored by increasing order (like 1, 2, 3, 4, 5), use the total order "<" implemented by: lambda x, y : x < y

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

## Description of functions

_BST(strict_total_order)_

-   O(1) time
-   takes a strict total order
-   returns an empty BST with that total order

_insert(tree, element)_

-   O(log(n)) time where n = size(tree)
-   takes a BST and an element
-   returns a BST with the elements of tree and element

_remove(tree, element)_

-   O(log(n)) time where n = size(tree)
-   takes a non-empty BST which contains element and an element
-   returns a BST with the elements of tree except for element

_contains(tree, element)_

-   O(log(n)) time where n = size(tree)
-   takes a BST and an element
-   returns true if element is in tree; false otherwise

_size(tree)_

-   O(n) time where n = size(tree)
-   takes a BST
-   returns the number of elements in tree

_is_empty(tree)_

-   O(1) time
-   takes a BST
-   returns true if tree if tree is an empty BST; false otherwise

_get_min(tree)_

-   O(log(n)) time where n = size(tree)
-   takes a non-empty BST
-   returns the minimum element of tree

_get_max(tree)_

-   O(log(n)) time where n = size(tree)
-   takes a non-empty BST
-   returns the maximum element of tree

_dump(tree)_

-   this is an impure function
-   O(n) time where n = size(tree)
-   takes a BST
-   prints the elements of tree
