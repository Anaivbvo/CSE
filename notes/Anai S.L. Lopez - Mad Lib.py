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
