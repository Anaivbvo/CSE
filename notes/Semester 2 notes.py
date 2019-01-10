print("hello world")  # write hello world in terminal

# Single line comment  # (write a single line comment)

cars = 5  # write variable cars = 5
driving = True  # write driving = true

print("I have %d cars." % cars)  # write i have 5 cars without writing 5 or five
print("I have " + str(cars) + " cars")  # str = string so it would add the string onto the print

old = input("How old are you? : ")  # ask the user for their age
print("Wow you're %s years old? You're ancient! :0!!" % old)  # use their age and write a remark against them

colors = ["red", "orange", "yellow", "green", "blue"]  # make a list with 5 colors
colors.append("purple")  # add onto the current list on top without editing so line

print(colors)  # show the list # computers count form 0 vv
colors.pop(0)  # first item from list without using the item's name (remove removes items, pop removes index/number)
print(colors)
print(colors[2])  # print the 3rd item in the list
print(len(colors)) #print legnth of the list
