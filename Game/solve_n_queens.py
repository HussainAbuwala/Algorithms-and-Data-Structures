def solve_n_queens(n):

    matrix = build_board(n)
    find_queens(matrix,0)


def build_board(n):

    mat = []
    for i in range(n):
        mat.append(['.'] * n)

    return mat


def find_queens(matrix,row):

    check = queen_safe(matrix)
    if check and row >= len(matrix):
        print_board(matrix)
        return
    elif check == False:
        return

    else:

        for i in range(len(matrix)):
            place_queen(row,i,matrix)
            find_queens(matrix,row+1)
            remove_queen(row,i,matrix)


def queen_safe(matrix):
    queen_pos = []

    for i,item in enumerate(matrix):
        for j,item2 in enumerate(item):
            if item2 == 'Q':
                queen_pos.append([i,j])

    for i in range(len(queen_pos)):
        for j in range(i+1,len(queen_pos)):
            if check_safe(queen_pos[i],queen_pos[j]) == False:
                return False
    return True


def check_safe(pos1,pos2):
    if pos1[0] == pos2[0]:
        return False
    if pos1[1] == pos2[1]:
        return False
    if abs(pos1[0] - pos2[0]) == abs(pos1[1] - pos2[1]):
        return False
    return True


def print_board(matrix):

    for i,item in enumerate(matrix):
        for j,item2 in enumerate(item):
            print(item2,end='  ')
        print()
    print()


def place_queen(row,i,matrix):
    matrix[row][i] = 'Q'

def remove_queen(row,i,matrix):
    matrix[row][i] = '.'

if __name__ == '__main__':
    solve_n_queens(8)
