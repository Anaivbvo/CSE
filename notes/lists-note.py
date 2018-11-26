# Creating a list
colors = ["blue", "turquoise", "pink", "orange", "black", "red"]
print(colors)
print(colors[1])
print(colors[0])

# Length of list
print("Thee are %d things in the list." % len(colors))

# Changing elements in a list
colors[1] = "Green"
print(colors)

# Looping through lists
for item in colors:
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