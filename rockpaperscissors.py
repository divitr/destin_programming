import random
moves = ["rock", "paper", "scissors"]
comp_score = 0
user_score = 0
while True:
    
    comp_move = random.choice(moves)
    user_move = input("what move: ")
    if user_move == "quit":
        print(user_score)
        print(comp_score)
        break
    if user_move == "rock" and comp_move == "paper":
        print("lose")
        comp_score = comp_score + 1
    if user_move == "rock" and comp_move == "scissor":
        print("win")
        user_score = user_score + 1
    if user_move == "rock" and comp_move == "rock":
        print("tie")
    if user_move == "paper" and comp_move == "rock":
        print("win")
        user_score = user_score + 1
    if user_move == "paper" and comp_move == "scissor":
        print("lose")
        comp_score = comp_score + 1
    if user_move == "paper" and comp_move == "paper":
        print("tie")
    if user_move == "scissor" and comp_move == "paper":
        print("win")
        user_score = user_score + 1
    if user_move == "scissor" and comp_move == "rock":
        print("lose")
        comp_score = comp_score + 1
    if user_move == "scissor" and comp_move == "scissor":
        print("tie")