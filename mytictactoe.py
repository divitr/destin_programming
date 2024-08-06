def move(player, board):
    if player == 1:
        symbol = "x"
    if player == 2:
        symbol = "o"
    row = int(input("row > "))      
    col = int(input("col > "))
def gameover(board):
    fill = "-"
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2]:
            return True
    for col in range(3):
        if board[col][0] == board[col][1] == board[col][2]:
            return True
    diag = board[1][1]
            
            