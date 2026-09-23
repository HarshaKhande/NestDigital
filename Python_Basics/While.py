"""'while' loop in Python, which repeatedly executes
a block of code as long as a condition remains True. Unlike for loops,
while loops are typically used when the number of iterations is not known
in advance.

Key Concepts:
- Basic while loop syntax
- While-else construct
- break and continue """

# basic while loop

count = 9
while count <=5:
    print(count)
    count  += 1

print ("Loop finsihed")

# while with else constrcut

n = 5
while n > 0:
    print(n)
    n-= 1
else:
    print("count down completed" )

# break  stop the execution
# continue -skip the execution

i =0
while True:  # intentinal infinite loop
    i+= 1
    if i > 5:
        break
    print(i)

# continue

i =0
while i < 10:
    i+= 1
    if i % 2== 0:
        continue
    print(i)

