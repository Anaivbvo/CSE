# Creating a list
color_list = ["blue", "turquoise", "pink", "orange", "black", "red"]
print(color_list)
print(color_list[1])
print(color_list[0])

# Length of list
print("There are %d things in the list." % len(color_list))

# Changing elements in a list
color_list[1] = "Green"
print(color_list)

# Looping through lists
for item in color_list:
    print(item)

"""
1. Make a list
2. Change the third thing in the list
3. Print the item
4. Print the full list
"""

sections = ["saxophone", "clarinet", "flute", "trumpet", "low brass", "drum line", "pit"]
print(sections)
sections[2] = "high wind boi-s"
print(sections)
print("The last thing in the list is %s." % sections[len(sections)-1])

# Slicing a list
print(sections[1:3])

food_list = ["sandwich", "burgers", "fries", "chicken", "buffalo wings", "salad", "tacos", "soup", "pancakes", "cake",
             "fish", "donuts", "cookies", "cake", "pizza", "pasta", "chips", "cob-corn", "pretzel", "lobster"]
print(food_list)
food_list.append("eggo waffles")
print(food_list)
food_list.remove("salad")
print(food_list)

"""
1. Make a list with 3 items
2. Add a 4th item to the list
3. Remove one of the first 3 items of the list
"""

milk_list = ["cow-regular", "chocolate", "almond"]
print(milk_list)
milk_list.append("strawberry")
print(milk_list)
milk_list.remove("almond")
print(milk_list)

# Tuples
brands = ("apple", "samsung", "HTC")  # Notice the parenthesis

# Also removing stuff from a list
print(food_list)
food_list.pop(0)
print(food_list)

# Find the index of an item
print(food_list.index("chicken"))

# Changing things into a list
string1 = "turquoise"
list1 = list(string1)
print(list1)

# Turn a list into a string
print("".join(list1))
print("!".join(list1))

"""

for i in range (len(list1)): # i goes through all indices
    if list1 == "u": # if we find a "u"
        list1.pop[1] # remove the i-th index
        list1.insert(i, "*") # Put a * there instead


for character in list1:
    if character == "u"
        "00#" replace with a "*"
        current_index = list1.index(character)
        list.pop(current_index)
        list1.insert(current_index. "*")
        
"""

# turn list into string
print("".join(list1))

# If you want add something int the quotations

"""
# Faction notes
# a**2 + b**2 = c**2
def pythagorean (a, b):
    return (a** + b**)**(1/2)


print(pythagorean(3, 4))
"""

day = input("How was your day? : ")
print("You had a %s day." % day)

verbA = input("Choose a past tense verb. : ")
print("You %s across the sky." % verbA)

print("Now for the real mad lib~!")

petA = input("Choose a singular noun, specifically a pet choice : ")
print("Oh hey look, there's a %s." % petA)
print("I wonder what adventures this %s will go on..." % petA)

""" 
verbB = input("Choose a verb : ")
verbC = input("Choose a new verb : ")
print("You are both %s and %s. " % (verbB, verbC))
"""

"""
print("Mad Lib")

people1 = input("Choose a group of people: ")
print(" The %s are quite strange." % people1)

adj1 = input("Choose an adjective: ")
adj2 = input("Choose another adjective: ")
print(" They tend to be very %s and %s at times." % (adj1, adj2))

task1 = input("Choose an everyday task: ")
adj3 = input("Choose a third adjective: ")
print(" Whenever you so happen to do %s hey react in such a %s manner. Maybe they don’t do %s." % (task1, adj3, task1))

adj4 = input("Choose a fourth adjective: ")
print(" Even their fashion sense is interesting. It's very %s and out of the ordinary." % adj4)

adj5 = input("Choose another adjective: ")
grade1 = input("Choose a grade level: ")
adj6 = input("Choose a sixth adjective: ")
print(" I wonder when they became so %s. Maybe it was when they entered %s grade. Everyone had a strange year during"
      "this grade. Everyone became %s." % (adj5, grade1, adj6))

adj7 = input("Choose another adjective: ")
print(" Yeah the %s are strange but %s. Hmm I wonder if we will ever truly know why." % (people1, adj7))

print("Final product: ")
print(" The %s are quite strange. They tend to be very %s and %s at times. Whenever you so happen to do %s hey react "
      "in such a %s manner. Maybe they don’t do %s. Even their fashion sense is interesting. It's very %s and out of "
      "the ordinary. I wonder when they became so %s. Maybe it was when they entered %s grade. Everyone had a strange"
      "year during this grade. Everyone became %s. Yeah the %s are strange but %s. Hmm I wonder if we will ever truly "
      "know why." % (people1, adj1, adj2, task1, adj3, task1, adj4, adj5, grade1, adj6, people1, adj7))
"""

myList = [0, 1, 2, 3, 4, 5]
myList. reverse()
print(myList)
