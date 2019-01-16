import random
colors = ["black", "brown", "red", "orange", "yellow", "green", "blue", "purple", "indigo", "violet"]
word = random.choices(colors)
print(word)

word2 = list(word)
print(word2)

print(word2.replace(word2, 'X'))
