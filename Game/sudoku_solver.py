def main(grid):

    cells = find_unassigned_cells(grid)
    sudoku_solver(grid,cells,0,0)


def find_unassigned_cells(grid):

    cells = []

    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] == 0:
                cells.append((i,j))
    return cells


def sudoku_solver(matrix,cells,prev,current):

    if prev < len(cells) and matrix[cells[prev][0]][cells[prev][1]] != 0:
        check = cell_safe(matrix,cells[prev][0],cells[prev][1])
        if check == False:
            return False
    if  current >= len(cells):
        print_board(matrix)
        return
    else:
        for j in range(1,len(matrix)+1):
            place_number(cells[current][0],cells[current][1],matrix,j)
            sudoku_solver(matrix,cells,current,current+1)
            remove_number(cells[current][0],cells[current][1],matrix)

def cell_safe(matrix,row,col):

    sudoku_row = matrix[row]
    numbers = []

    for item in sudoku_row:
        if item !=0 and item not in numbers:
            numbers.append(item)
        elif item == 0:
            continue
        else:
            return False

    numbers = []

    down_row = 0
    down_col = col

    while down_row < len(matrix) and down_col < len(matrix):
        if matrix[down_row][down_col] !=0 and matrix[down_row][down_col] not in numbers:
            numbers.append(matrix[down_row][down_col])
            down_row += 1
        elif matrix[down_row][down_col] ==0 :
            down_row += 1
        else:
            return False

    return True

def print_board(matrix):

    for i,item in enumerate(matrix):
        for j,item2 in enumerate(item):
            print(item2,end='  ')
        print()
    print()



def place_number(row,col,matrix,number):
    matrix[row][col] = number

def remove_number(row,col,matrix):
    matrix[row][col] = 0


if __name__ == '__main__':
    grid = [      [0, 5, 4, 8, 0, 2, 7, 1, 0],
                  [2, 0, 0, 0, 0, 0, 0, 0, 5],
                  [8, 0, 3, 4, 0, 7, 9, 0, 6],
                  [5, 0, 6, 0, 0, 0, 1, 0, 4],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [7, 0, 1, 0, 0, 0, 3, 0, 9],
                  [6, 0, 5, 1, 0, 3, 2, 0, 8],
                  [4, 0, 0, 0, 0, 0, 0, 0, 1],
                  [0, 9, 8, 2, 0, 5, 6, 3, 0]]

    grid2 = [[0,1,0,0,0],
             [0,0,0,3,0],
             [0,0,4,0,0],
             [1,0,0,5,0],
             [3,0,0,0,4]]
    main(grid)

