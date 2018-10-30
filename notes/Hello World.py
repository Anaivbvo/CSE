"""
print("Hello World!")

# This is a comment, This had no effect on the code
# but this does allow me to do things, I can:
# 1. Make notes to myself
# 2. Comment pieces of code does not work
# 3. Make my code easier to read

print("Look at what happens here. Is there any space?")
print("")
print("")
print("There should be a couple of blank lines here.")

# Math
print(3+5)
print(5-2)
print(3*4)
print(6/2)

print("Figure this out...")
print(6//2)
print(5//2)
print(9//4)

print("Here is another one...")
print(6%2)
print(5%2)
print(11%4)


# Whats is 2^100?
print(2**100)

# Taking input
name = input ("What is your name?")
print("Hello %s." % name)

age = input("How old are you? >_")
print("%s?!? You belong in a museum." % age)
print()
print("%s is really old. They are %s years old." % (name,age))
uhhhh
uhuhuhu
hhhhhhhhhh
hhh
hhh
hhh
hhh
hhh
hhh
hhh
hhh
hhh
hhh
hhh
hhh
"""

"""
This is a multi line comment
"""


# Functions
def say_it():
    print("Hello World!")


say_it()
say_it()
say_it()


# f(x) = 2x + 3
def f(x):
    print(2*x + 3)


f(1)
f(5)
f(5000)


# distance formula
def distance(x1, y1, x2, y2):
    dist = ((x2-x1)**2 + (y2-y1)**2)**(1/2)
    print(dist)


distance(0, 0, 3, 4)
distance(0, 0, 5, 12)

# Loops
for i in range(5) : # This gives the number 9
    say_it()

for i in range(10) :
    print(i + 1)

for i in range(5) :
    f(i)