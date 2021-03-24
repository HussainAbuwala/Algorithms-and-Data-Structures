def find_all_paths_above_diagonal(i,j,string,m,n,arr):

    if(i == m-1 and j == n-1):
        arr.append(string)

    elif(i == j and check_grid_index_valid(i,j+1,m,n) == True):
        #only go right
        find_all_paths_above_diagonal(i,j+1,string + "0",m,n,arr)

    else:

        #go right
        if(check_grid_index_valid(i,j+1,m,n) == True):
            find_all_paths_above_diagonal(i, j + 1, string + "0", m, n,arr)
        #go down
        if(check_grid_index_valid(i+1,j,m,n) == True):
            find_all_paths_above_diagonal(i + 1, j, string + "1", m, n,arr)

def find_target_path_above_diagonal(i,j,string,m,n,arr,target,store):

    if(i == m-1 and j == n-1):
        arr.append(string)
        if(bin_to_dec(string) == target):
            store.append(len(arr))

    elif(i == j and check_grid_index_valid(i,j+1,m,n) == True and store == []):
        #only go right
        find_target_path_above_diagonal(i,j+1,string + "0",m,n,arr,target,store)
    else:
        if(check_grid_index_valid(i,j+1,m,n) == True and store == []):
            find_target_path_above_diagonal(i, j + 1, string + "0", m, n,arr,target,store)

        #go down
        if(check_grid_index_valid(i+1,j,m,n) == True and store == []):
            find_target_path_above_diagonal(i + 1, j, string + "1", m, n,arr,target,store)


def find_target_path_pos(N,tree_code):

    target = bin_to_dec(tree_code[0:len(tree_code) - 1])
    arr = []
    store = []
    find_target_path_above_diagonal(0, 0, "", N + 1, N + 1, arr, target, store)
    return store[0]


def check_grid_index_valid(i,j,m,n):

    if(i < m and j < n):
        return True
    return False

def bin_to_dec(binary_num):
    return int(binary_num,2)

def find_all_trees(N):

    arr = []
    find_all_paths_above_diagonal(0, 0, "", N + 1, N + 1, arr)
    for i in range(len(arr)):
        arr[i] = arr[i] + "1"
        arr[i] = bin_to_dec(arr[i])

    return arr


if __name__ == '__main__':
    #print(len(find_all_trees(10)))
    pass