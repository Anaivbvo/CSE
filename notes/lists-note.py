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
brands = ("apple", "samsung", "HTC") # Notice the parenthesis

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


# Faction notes
# a**2 + b**2 = c**2
def pythagorean (a, b):
    return (a** + b**)**(1/2)


print(pythagorean(3, 4))
