rows, cols = 3, 3
Board = [["-"]*cols]*rows
while True:
    symbol = input("symbol")
    row = int(input("row?"))
    Col = int(input("col?"))
    Board[row-1][Col-1] = symbol
    print(Board)