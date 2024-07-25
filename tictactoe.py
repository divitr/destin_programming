rows, cols = 3, 3
def threeinarow(board):
    for row in range(rows):
        if Board[row][0] == Board[row][1] == Board[row][2]:
            return True
    return False
Board = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
while True:
    symbol = input("symbol")
    row = int(input("row?"))
    Col = int(input("col?"))
    Board[row-1][Col-1] = symbol
    print(Board)