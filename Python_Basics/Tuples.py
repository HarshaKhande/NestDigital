#A Tuple in Python is used to store multiple values in a single variable.

# ordered and imutable in nature and also allows dulpicate  values

#List  → mutable → can be changed
#Tuple → immutable → cannot be changed

# empty tuple
empty_tuple = ()
print(empty_tuple)

# tuple with elements
numbers12 = (1, 2, 3, 4, 5,5)
fruits = ("apple", "banana", "cherry")
mixed = (1, "hello", 3.14, True, None)
print(len(mixed))

print(f"Numbers: {numbers12}")
print(f"Fruits: {fruits}")
print(f"Mixed types: {mixed}")


# tuple modifiction

numbers = (10,20,30,40,50)
#numbers[1] = 25
# convert the tuple to a list
temp = list(numbers)
temp[1] = 25
numbers1 = tuple(temp)
print(numbers1)

for num in numbers:
    print(num)

# Tuple can contain different data types
data = ("Anurag", 23, 85.5, True)
print(data)


# count - how many times a value is repeated
print(numbers12.count(5))

# index
numbers = (10, 20, 30, 40)
print(numbers.index(30))





