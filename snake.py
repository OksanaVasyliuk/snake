
def game_board (size=10):
    table = []
    for a in range(size):
        row = []
        for b in range(size):
            row.append(".")
        table.append(row)
    return table

def print_board (table):
    print("Game board:")
    for row in table:
        for value in row:
            print("{}".format(value), end=" ")
        print()

table=game_board()
print (table)


def draw_board(table,x,y):
    table[x-1][y-1]="X" 
    return table

print (draw_board(table,2,2))
print_board(table)