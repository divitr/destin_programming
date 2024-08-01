rows, cols = 3, 3
def threeinarow(board):
    for row in range(rows):
        if Board[row][0] == Board[row][1] == Board[row][2]:
            return True
    return False
def threeinacolumn(board):
    for cols in range(cols):
        if Board[0][cols] == Board[1][cols] == Board[2][cols]:
            return True
    return False
def threeinadiagonal(Board):
    if Board[0][0] == Board[1][1] == Board[2][2]:
        return True
    if Board[0][2] == Board[1][1] == Board[2][0]:
        return True
    return False

Board = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]

while True:
    symbol = input("symbol")
    row = int(input("row?"))
    Col = int(input("col?"))
    Board[row-1][Col-1] = symbol
    print(Board)
    if threeinarow(Board) or threeinacolumn(Board) or threeinadiagonal(Board) == True:
        print("gg")
        break
