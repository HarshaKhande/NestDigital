# for loop in python is used to iterate over the sequences (list, tuples, strings , ranges )

# basic for loop
# range () function
# itearting over diff dataypes
# enumerate for index and value
# zip ()  for parallel ietration
# nested for loops

# basic for loop

fruits = ["apple", "banana", "cherry", "date"]
for fruit in fruits:
    print(f"I like {fruit}")

# range function  - start , stop and step - generate the numbeers from nstart to stop -1
for i in range(5):
    print(i)

for i in range(2,8):
    print(i)

for i in range(0,10,3):
    print(i)


# iterating  over diff dataypes

# string data type
word = "python"
for char in word:
    print(f" {char}")

items = [1, "John" , 78.98]
for item in items:
    print(item)

#enumerate for index and value

languages = ["Python", "JavaScript", "C++", "Rust"]

for  lang, index in enumerate(languages):
    print(index, lang)


# zip function - # zip() combines multiple iterables and iterates over them together

names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
cities = ["New York", "London", "Tokyo"]

for city,name,age in zip(names,ages,cities):
    print(city,name,age)

# nested for loops

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


# Row-by-row iteration
for row in matrix:
    for item in row:
        print(item, end=" ")
    print()  # Moves to the next line after each row finishes

# else with for loop

numbers = [1,3,5,7,9]
search_for = 10

for num in numbers:
    if num == search_for:
        print (f"Found {search_for}")
        break
else:
    print(f"{search_for} was not found")





