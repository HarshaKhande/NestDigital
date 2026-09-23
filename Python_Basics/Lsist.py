# lists - ordered , mutable , they can store the elements of any data types , it allows duplicate e values

# Creating and accessing of the lists
# list methods (append , insert , remove , pop)
# slicing and indeixng
# list operations (conctenation and repetition)
# list comprehensions


# empty list
empty_list = []
print(empty_list)

# list with elements
numbers = [1, 2, 3, 4, 5]
fruits = ["apple", "banana", "cherry"]
mixed = [1, "hello", 3.14, True, None]
print(len(mixed))

print(f"Numbers: {numbers}")
print(f"Fruits: {fruits}")
print(f"Mixed types: {mixed}")

# list from range function

range_list = list(range(1,6))
print(range_list)

# accesing the elements - indexing

print(fruits[1]) # banana
print(mixed[4])


#list methods (append , insert , remove , pop)

items = [1,2,3]
print(items)
items.append(4)
print(items)

# add multiple elements
items.extend([5,6])
print(items)

# insert() - add lement at a spef=cific postion
items.insert(0,0)
print(items)


# remove the elements - remove the first occurence of the value
items.remove(3)
print(items)

# pop - remove and return elements at index
popped = items.pop()
print([popped])

items.reverse()
print(items)

items.clear()
print(items)


numbers = [1, 2, 2, 3, 4, 4, 5]

unique_numbers = list(set(numbers))

print(unique_numbers)


# list slicing
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"Original: {nums}")

print(f"{nums[2:5]}")
print(f"{nums[1:6]}")
print(f"{nums[:4]}") # first 4 elements
print(f"{nums[6:]}") # from index 6 to end
print(f"{nums[::2]}") # every 2nd element
print(f"{nums[::-1]}") # reverse the list

#list (conctenation and repetition)

list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1+list2
print(combined)


# repetition
repeated = [0] * 5
print(repeated)

#list comprehensions - shoter synatx - one liner
square = [x**2 for x in range (1,6)]
print(square)

even_sq = [x**2 for x in range(1,11) if x % 2 ==0]
print(even_sq)



