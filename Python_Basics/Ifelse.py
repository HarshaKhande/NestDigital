# conditional statements

#Key Concepts:
#- if statement: Executes code block if condition is True
#- else statement: Executes code block if condition is False

# simple if statement

age = 16

if age >= 18:
    print("You are a adult")
else:
    print("You are minor")

# combine multiple conditions
age = 12
has_license = True

if age>=18 and has_license:
    print("You can drive a car")
else:
    print("You cant drive")

# nested if statement  - if statemnet inside other if statement

score = 40
attendance = 90

if score >=60:
    print("YOu passed the exams")
    if attendance >=80:
        print("You have execellent attendance")
    else:
        print("Try to improve your attendance")
else:
    print("You need to study harder")


