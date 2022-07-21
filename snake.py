
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


def draw_board(table,coordinates):
    for i in coordinates:
        x_y=i
        for j in x_y:
            x=x_y[0]
            y=x_y[1]
        table[x][y]="X" 
    return table

print (draw_board(table,([(0,0),(2,4), (3,5),(6,9)])))

print_board(table)
