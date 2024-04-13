import random

def choose_word():
    with open("five_letter_words.txt", "r") as file:
        words = file.read().splitlines()
    return random.choice(words), words
    
def check_guess(word, guess):
    l = []
    for i in range(len(guess)):
        if word[0] == guess[i]:
            l.append('green')
        elif guess[i] in word:
            l.append('yellow')
        else:
            l.append('black')
        word = word[1:]
    return [(guess[i], l[i]) for i in range(len(l))]

def parse(check_result):
    res =  len('Guess a 5 Letter Word: ')*' '
    for result in check_result:
        if result[1] == 'black':
            res = res + ("\u2B1B")
        elif result[1] == 'yellow':
            res = res + ("\U0001F7E8")
        else:
            res = res + ("\U0001F7E9")
    return res

### CLI ###
def play():
    remaining_guesses = 6
    word, words = choose_word()
    while remaining_guesses > 0:
        guess_is_not_valid = True
        while guess_is_not_valid:
            guess = input("Guess a 5 Letter Word: ")
            if len(guess) != 5:
                print("Not 5 Letters")
            elif not (guess in words):
                print("Not a Valid Word")
            else:
                guess_is_not_valid = False
                remaining_guesses = remaining_guesses - 1
        check_result = check_guess(word, guess)
        print(parse(check_result))
        if all([check_result[i][1] == 'green' for i in range(len(check_result))]):
            print("Congrats!")
            return
    print(f"Out of guesses, the correct word was {word}")

play()