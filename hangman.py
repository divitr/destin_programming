import random
fruits = ["mango", "apple", "banana", "orange", "blueberry", "Lime", "Advocado"]
fruitname = random.choice(fruits)
list = []
x = len(fruitname)
for i in range(x):
    list.append("_")
for i in range(15):
    guess = input("guess: ")
    if guess in fruitname:
        list.remove("_")
        list.append(guess)
        print(guess)        