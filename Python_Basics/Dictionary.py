#A Python dictionary is used to store data in key–value pairs.

student = {
    "name": "John",
    "age": 23,
    "course": "Python"
}

print(student)
print(student["name"])
print(student["age"])


# add a new item
student["city"] = "Bangalore"
print(student)

# modify the exiesting data
student["age"] = 45
print(student)

# remove an item
student.pop("age")
print(student)

# get all keys and values
print(student.keys())
print(student.values())
print(len(student))



#Dictionary with different data types

employee = {
    "name": "Anurag",
    "age": 23,
    "salary": 45000.50,
    "is_active": True,
    "skills": ["Python", "Playwright", "Testing"]
}

print(employee["skills"])

