# string is seq of characters - sinle quotes or double quotes

name = "John tony jimmy"
course = 'Python'

print(name)
print(course)
print(name.title())


# multi line string
message = """ hello how are you 
welcome to Banaglore
"""

print(message)

# slicing - extract a part of string

text = "python"

print(text[0:2]) #py
print(text[2:5]) #tho
print(text[0:4]) #pyth


# negative indexing

print(text[-1])
print(text[-3])

# modifying the string

# in python strings are immutable in nature - we cannot change the value directly
# convert to uppercase

text = "hello world"
print(text.upper())
print(text.capitalize())

# lowercase

print(text.lower())

# captailize the first letter

print(text.capitalize())

# captailize the first leter in the word  word

print(text.title())

text = " hello world "
print(text.strip())

# replace the string

text = "Java program"

new_text = text.replace("Java" , "python")
print(new_text)

# split of the string

text = "apple,banana,mango"

fruits = text.split(",")

print(fruits)

# joining of the strings

words = ["Hello", "Python", "World"]
text = "_".join(words)

print(text)

# concatenation

String1 = "King"
String2 = "Queen"

String3 = String1 + String2
print(String3)


# escape characters begining with \

print("Hello\nPython")

# tab \t

print("Name\tAge")

# format strings - to insert variables or values inside a string

name = "Anurag"
age = 25
height = 1.75

print(f"My name is {name} and I am {age} years old")


a = 10
b = 20

print(f"Sum = {a+b}")






















