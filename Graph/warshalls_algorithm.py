from lab_1 import multiply_two_matrices
def warshalls_transitive_closure(graph):


    for k in range(len(graph)):
        for i in range(len(graph)):
            for j in range(len(graph)):
                if graph[i][j] == 1:            #if there is already a path, then connectivity already exists
                    continue
                if graph[i][k] == 1 and graph[k][j] == 1:   # if we can make connectivity by adding some intermediate vertes, why not connect it.
                    graph[i][j] =1
                else:
                    continue                            #else it is not connected

    return graph

    #time comlexity is O(|V|^3)

def multiply_row_and_column(row,matrix,row1,col1,matrix1):

    actual_row = matrix[row]

    sum = 0
    for i in range(len(actual_row)):
        sum = sum + actual_row[i] * matrix1[row1][col1]
        row1 +=1

    return sum

def matrix_multiply(matrix,matrix1):


    new_matrix = []

    for i in range(len(matrix)):
        new_matrix.append([None] * len(matrix))

    for index,item in enumerate(matrix):
        for i in range(len(item)):
            new_matrix[index][i] = multiply_row_and_column(index,matrix,0,i,matrix1)

    return new_matrix

def naive_transitive_closure(graph):


    y = graph
    x = graph

    new_matrix = []

    for i in range(len(graph)):
        new_matrix.append([0] * len(graph))

    new_matrix = check_matrix(new_matrix,graph)

    for i in range(len(graph)):                 #the adjacency matrix is exponieted |V| times
        x = matrix_multiply(x,y)
        new_matrix = check_matrix(new_matrix,x) # in the ith iteration, we get a matrix which has number of walks of length exactly i

    # total cmplexity is O(|V| * |V|^3) = O(|V|^4)
    return new_matrix

def check_matrix(original_graph,temp_graph):

        for i,item in enumerate(temp_graph):
            for j,item2 in enumerate(item):
                if item2 > 0:
                    original_graph[i][j] = 1

        return original_graph



if __name__ == '__main__':

    graph = [[0,1, 0, 0, 1],
            [0, 0, 0, 1, 1],
            [0, 0 , 0 , 0,0],
            [0, 0, 1, 0, 0],
            [1, 0, 0, 1, 0]]

    print(naive_transitive_closure(graph))