from circular_queue import Circular_Queue
import timeit

def find_neighbours(vertice,width,height,matrix):
    """
                This function finds the neighbours of the vertices
                :param vertice: vertices of which the neighbours are to be found
                :param width: width of the maze
                :param height: height of maze
                :param matrix: maze
                :return: neighbours
                :raises: None
                :precondition: valid parameters
                :complexity: best and worst case is O(1).
                :postcondition: neighbours found
                """

    neighbours = []
    x = vertice[0]
    y = vertice[1]
    if y + 1 > -1 and y + 1 <width:
        if matrix[x][y+1] != 0:
            neighbours.append((x,y + 1))
    if y - 1 > -1 and y - 1 < width:
        if matrix[x][y - 1] != 0:
            neighbours.append((x,y-1))
    if x + 1 >-1 and x + 1 < height:
        if matrix[x+1][y] != 0:
            neighbours.append((x+1,y))
    if x - 1 > -1 and x -1 < height:
        if matrix[x-1][y] != 0:
            neighbours.append((x-1,y))
    return neighbours
def return_path_iterative(parent,temp,matrix):
    """
                    This function finds the shortest path by backtracking
                    :param parent: 
                    :param temp: parent
                    :param matrix: maze
                    :return: None
                    :raises: None
                    :precondition: valid parameters
                    :complexity: best and worst case is O(m) where m is the length of the shortest path.
                    :postcondition: shortest path found
                    """

    while True:
        if temp == None:
            break
        if parent[temp[0]][temp[1]] == None:
            matrix[temp[0]][temp[1]] = '*'
            break
        else:
            matrix[temp[0]][temp[1]] = '*'
            temp = parent[temp[0]][temp[1]]
def read_maze(input_filename,output_filename):
    """
                    This function reads the maze
                    :param input_filename: input file
                    :param output_filename: output file
                    :return: None
                    :raises: None
                    :precondition: valid parameters
                    :complexity: best and worst case is O(N*M) where N is height of maze and M is width of maze
                    :postcondition: maze read
                    """

    file = open(input_filename, "r")
    matrix = []
    i=0
    j=0
    start=()
    end = ()

    x = []

    for item in file:
        string = item.strip('\n')
        new_array = []
        j = 0
        for item in string:
            if item == '.' or item == 'S' or item == 'F':
                if item == 'S':
                    start = (i,j)
                if item == 'F':
                    end = (i,j)
                new_array.append(1)
            else:
                new_array.append(0)

            j+=1
        i+=1

        matrix.append(new_array)

    width = len(matrix[0])
    height = len(matrix)

    visited = []
    parent = []

    for i in range (height):
        visited.append([False] * width)
        parent.append([None] * width)

    visited[start[0]][start[1]] = True
    parent[start[0]][start[1]] = None

    bfs_find_shortest_path(visited,parent,width,height,matrix,start)
    return_path_iterative(parent, end, matrix)
    output_maze(matrix,output_filename)
def bfs_find_shortest_path(visited,parent,width,height,matrix,start):
    """
                        This function finds the shortest path by bfs
                        :param visited: visited matrix
                        :param parent: parent matrix
                        :param width: width of maze
                        :param height: height of maze
                        :param matrix: matrix
                        :param start: starting point
                        :return: None
                        :raises: None
                        :precondition: valid parameters
                        :complexity: best and worst case is O(|V| + |E|) where |V| is the number of vertices and |E| is number of edges
                        :postcondition: graph traversed
                        """
    queue = Circular_Queue()
    queue.append(start)

    while not queue.is_empty():
        x = queue.serve()
        neighbours = find_neighbours(x,width,height,matrix)
        for item in neighbours:
            if visited[item[0]][item[1]] == False:
                parent[item[0]][item[1]] = x
                queue.append(item)
                visited[item[0]][item[1]] = True
def output_maze(matrix , output_filename):
    """
                        This function outputs the maze
                        :param matrix: maze
                        :param output_filename: output file
                        :return: None
                        :raises: None
                        :precondition: valid parameters
                        :complexity: best and worst case is O(N*M) where N is height of maze and M is width of maze
                        :postcondition: maze output with shortest path
                        """


    file = open(output_filename,'w')
    for i in range(len(matrix)):
        row = matrix[i]
        string = ''
        for j in range(len(row)):
            if (row[j] == 0):
                string += '#'
            elif (row[j] == 1):
                string += '.'
            elif (row[j] == '*'):
                string += 'o'

        file.write(string + '\n')

if __name__ == '__main__':
    starts = timeit.default_timer()
    read_maze('large_maze.txt','solution.txt')
    taken = (timeit.default_timer() - starts)
    print(taken)

