print("Mad Lib")

list1 = []

list1.append(input("Choose a group of people: "))
print(" The %s are quite strange." % list1[0])

list1.append(input("Choose an adjective: "))
list1.append(input("Choose another adjective: "))
print(" They tend to be very %s and %s at times." % (list1[1], list1[2]))

list1.append(input("Choose an everyday task: "))
list1.append(input("Choose a third adjective: "))
print(" Whenever you so happen to do %s hey react in such a %s manner. Maybe they don’t do %s." % (list1[3], list1[4],
                                                                                                   list1[3]))

list1.append(input("Choose a fourth adjective: "))
print(" Even their fashion sense is interesting. It's very %s and out of the ordinary." % list1[5])

list1.append(input("Choose another adjective: "))
list1.append(input("Choose a grade level: "))
list1.append(input("Choose a sixth adjective: "))
print(" I wonder when they became so %s. Maybe it was when they entered %s grade. Everyone had a strange year during"
      "this grade. Everyone became %s." % (list1[6], list1[7], list1[8]))

list1.append(input("Choose another adjective: "))
list1.append(input("Choose a finale adjective: "))
print(" Yeah the %s are strange but %s. Hmm I wonder if we will ever truly know why." % (list1[9], list1[10]))

print("Final product: ")

print(" The %s are quite strange." % list1[0])
print(" They tend to be very %s and %s at times." % (list1[1], list1[2]))
print(" Whenever you so happen to do %s hey react in such a %s manner. Maybe they don’t do %s." % (list1[3], list1[4],
                                                                                                   list1[3]))
print(" Even their fashion sense is interesting. It's very %s and out of the ordinary." % list1[5])
print(" I wonder when they became so %s. Maybe it was when they entered %s grade. Everyone had a strange year during"
      "this grade. Everyone became %s." % (list1[6], list1[7], list1[8]))
print(" Yeah the %s are strange but %s. Hmm I wonder if we will ever truly know why." % (list1[9], list1[10]))
