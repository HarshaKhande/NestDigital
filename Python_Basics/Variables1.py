#Variables are used to store the data

# variable creation
# assignment
# variable naming conventions
# mutliple assignments
# variable type checking
# constants
# scope of variables

# simple variable assignments

name = "John"
empid = 45556
height = 1.75
is_student = True

print(name,empid,height)
print(empid)
print(height)
print(is_student)

# variables can be reassigned to different values

x = 10
print(x)
x = 20
print(x)

# variables can even change the types (dynamic typing)

value = 100
print(value)
value = "hundred"
print(value)

# variable naming rules

y = "ghj" # lowercase
myVariable = "tyyuu" # camel case
_var = 677678 # variable with underscore
var123 = 54566 # can contain numbers but do not start with them
CONSTANT = 677878 # capital letters is also allowed

# mutliple assignmnets

a = b = c = 50
print(a,b,c)
print(type(a))

# type checking of the variables

str = "Jenny"
print(type(str))

# constants - Math

PI = 3.14576878
RATIO = 67.89

MAX_USERS= 100
API_TIMEOUT = 30

# scope of vraiables - global and local scope

# global variable
message = "Hello from the global scope"
print(message)
print(str)


def read_global():
    # You can read it directly
    str = "Hello"
    print(message)
    print(str)

read_global()



















