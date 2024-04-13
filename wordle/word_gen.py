import enchant
from tqdm import tqdm

d = enchant.Dict("en_US")

five_letter_words = []

for i in tqdm(range(ord('a'), ord('z')+1)):
    for j in range(ord('a'), ord('z')+1):
        for k in range(ord('a'), ord('z')+1):
            for l in range(ord('a'), ord('z')+1):
                for m in range(ord('a'), ord('z')+1):
                    word = chr(i) + chr(j) + chr(k) + chr(l) + chr(m)

                    if d.check(word):
                        five_letter_words.append(word)

with open('five_letter_words.txt', 'w') as file:
    for word in five_letter_words:
        file.write(word + '\n')

print("txt file generated successfully!")