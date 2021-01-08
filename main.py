from binary_tree import BST, insert, remove, is_empty, size, contains, dump, get_min, get_max
from functools import reduce

# Dog class
class Dog:
	def __init__(self, name, age):
		self.name = name
		self.age = age

dog1 = Dog("Brownie", 1)
dog2 = Dog("Jack", 8)
dog3 = Dog("Spark", 4)
dog4 = Dog("Ruby", 4)
dogs = [dog1, dog2, dog3, dog4]

# order by "<" on age first, then alphabetically on name
def strict_total_order(dog1, dog2):
	age1 = dog1.age
	age2 = dog2.age
	name1 = dog1.name.lower()
	name2 = dog2.name.lower()
	if age1 != age2:
		return age1 < age2
	elif name1 != name2:
		return sorted([name1, name2])[0] == name1
	else: #names and age are equal
		return False

empty_bst = BST(strict_total_order)

dogs_bst = reduce(insert, dogs, empty_bst)

print(contains(dogs_bst, dog1))
print(contains(dogs_bst, Dog("Bear", 2)))
print(get_min(dogs_bst).name)
print(size(dogs_bst))