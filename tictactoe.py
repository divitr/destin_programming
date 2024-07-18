rows, cols = 3, 3
Board = [["-"]*cols]*rows
while True:
    x = input("player1: ")
    y = input("player2: ")
    if x == "0,1":
        Board[0][0] = "X"
        print(Board)
    if x == "0,2":
        Board[0][1] = "X"
        print(Board)
    if x == "0,3":
        Board[0][2] = "X"
        print(Board)
    if x == "1,0":
        Board[0][0] = "X"
        print(Board)