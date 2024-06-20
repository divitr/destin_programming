import random
fruits = ["mango", "apple", "banana", "orange", "blueberry", "Lime", "Advocado"]
fruitname = random.choice(fruits)
x = len(fruitname)
for i in range(x):
    list.append("")
for i in range(15):
    guess = input("guess: ")
    if guess in fruitname:
    