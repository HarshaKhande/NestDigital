""" A set in Python is a collection of unique values.

The important points are:

Set:
- does not allow duplicate values
- is unordered
- is mutable
- is written using { }  """


# empty set
empty_set = {}
print(empty_set)

# set with elements
numbers12 = {1, 2, 3, 4, 5,5}
fruits = {"apple", "banana", "cherry"}
mixed = {1, "hello", 3.14, True, None}
print(len(mixed))

print(f"Numbers: {numbers12}")
print(f"Fruits: {fruits}")
print(f"Mixed types: {mixed}")

# add method

fruits = {"apple", "banana"}
fruits.add("orange")
print(fruits)

#Add multiple items
#Use update():

fruits = {"apple", "banana"}
fruits.update(["orange", "mango", "grapes"])
print(fruits)

#Remove an item

#Using remove():
fruits = {"apple", "banana", "orange"}
fruits.remove("banana")
print(fruits)


#pop()

#pop() removes an arbitrary item.
fruits = {"apple", "banana", "orange"}
removed = fruits.pop()
print("Removed:", removed)
print(fruits)


# set operations -

# union -#Union gives all unique values from both sets.

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

result = set1.union(set2)
print(result)


# intersection - Intersection gives common values.
result = set1.intersection(set2)
print(result)

# difference -#Values present in set1 but not in set2:
result = set1.difference(set2)
print(result)

# issubset -Checks whether one set is completely contained inside another.
a = {1,2,5}
b = {1,2,3,4}
print(a.issubset(b))


