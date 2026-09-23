

# artimetic operators

a = 10
b= 3

print("Addition" , a + b) #13
print("Substraction" , a - b) #7
print("Multiply" , a * b) #30
print("Div" , a / b) #3.33
print("Modulus" , a % b ) #1
print("Floor Divison" ,  a // b) #3
print("Power" , a ** b) #1000


# relational operators

x = 10
y = 20

print("Equal" ,  x ==y) # false
print("NOt Equal" ,  x !=y) # True
print("Greater than " ,  x > y) # false
print("Less than" ,  x < y) # True
print("Greater than or equal " ,  x >= 10) # True
print("Lesser  than " ,  x <= 20 ) # True


# logical operators

age = 25
has_license = True

print("AND:" , age>= 18 and has_license)
print("OR:" , age < 18 or has_license)
print("NOT:" ,  not has_license)

# bitwise operators

a = 5
b =3

print("Bitwise AND", a & b) #1
print("Bitwise OR" , a | b) # 7
print("Bitwose XOR", a ^ b) #6
print("Bitwise NOT", ~a) # -6


# shift operators

number = 5
number1 = 20

print ("Left shift" , number << 1) #10
print("right shift" , number1 >> 2 ) # 5


# assignment operators

x = 10
print("Initial value" , x)

x+=5
print(x)

x-=3
print(x)

x*=2
print(x)

x/=2
print(x)

x//2
print(x)

x%=2
print(x)

x**=3
print(x)

# identity operators

list1 = [1,2,3]
list2 = [1,2,3]
list3 = [1,2,4]


print(list1 is list2) # True
print(list1 is list3) # false

print(list1 is not list3) # true


# membership operators

fruits = ["apple", "banana", "mango"]

print("apple in fruits", "apple" in fruits)  # true

print("apple in fruits", "kiwi" not in fruits)  # true