from random import randrange

def print_board (table):
    print("Game board:")
    for row in table:
        for value in row:
            print("{}".format(value), end=" ")
        print()

table = [
    ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
     ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'], 
     ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],       ['.', '.', '.', '.', '.', 'X', '.', '.', '.', '.'], 
      ['.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']]

def fruit ():
    coordinates=[]
    for i in range(2):
        coordinates.append(randrange(0,9))
    return coordinates

def fruit_on_board(table, coordinates):
    for i in coordinates:
        x=coordinates[0]
        y=coordinates[1]
    if table[x][y]!="X":
        table[x][y]="@"
    else:
        raise ValueError

while True:
    coordinates=fruit()
    try:
        fruit_on_board(table,coordinates)
    except ValueError:
        print("error")
        coordinates=fruit()
        fruit_on_board(table,coordinates)
    print_board(table)
