import numpy as np

def turn(player, board):
    assert player == 1 or player == 2
    symbol = "x"
    if player == 2:
        symbol = "o"
    row = int(input("row > ")) #zero indexed
    col = int(input("col > ")) #zero indexed
    
    board[row][col] = symbol

def gameover(board):
    filler_symbol = "-"

    # rows
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] and board[row][0] != "-":
            return True
    
    #cols
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != "-":
            return True
        
    #diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[1][1] != "-":
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[1][1] != "-":
        return True
    
    #if no 3 in a row found, return false
    return False

def gameloop():
    board = np.full((3,3), "-")
    player = 1
    while True:
        turn(player, board)
        print(board)
        if gameover(board):
            print("GAME OVER")
            return
        
        # switching players
        if player == 1:
            player = 2
        else:
            player = 1

gameloop()
        




### DESTIN'S CODE ###


# rows, cols = 3, 3
# def threeinarow(board):
#     for row in range(rows):
#         if Board[row][0] == Board[row][1] == Board[row][2]:
#             return True
#     return False
# def threeinacolumn(board):
#     for cols in range(cols):
#         if Board[0][cols] == Board[1][cols] == Board[2][cols]:
#             return True
#     return False
# def threeinadiagonal(Board):
#     if Board[0][0] == Board[1][1] == Board[2][2]:
#         return True
#     if Board[0][2] == Board[1][1] == Board[2][0]:
#         return True
#     return False

# Board = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]

# while True:
#     symbol = input("symbol")
#     row = int(input("row?"))
#     Col = int(input("col?"))
#     Board[row-1][Col-1] = symbol
#     print(Board)
#     if threeinarow(Board) or threeinacolumn(Board) or threeinadiagonal(Board) == True:
#         break
        