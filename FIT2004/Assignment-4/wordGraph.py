from circular_queue import Circular_Queue
import timeit

def mergeSort(alist,m):
    """
                        This function sorts
                        :param alist: input list
                        :param m: which comparison function to use
                        :return: None
                        :raises: None
                        :precondition: valid parameters
                        :complexity: best and worst case is O(NlogN) where N is the length of the list
                        :postcondition: list sorted
                        """
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf,m)
        mergeSort(righthalf,m)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if compare(lefthalf,righthalf,i,j,m):
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1

    return alist
def compare(lefthalf,righthalf,i,j,m):
    """
                        This function reads the maze
                        :param lefthalf: item1
                        :param righthalf: item2
                        :param i: index
                        :param j: index
                        :param m: index
                        :return: None
                        :raises: None
                        :precondition: valid parameters
                        :complexity: best and worst case is O(1)
                        :postcondition: comparison done
                        """
    if m==1:
        if lefthalf[i][len(lefthalf[i]) - 1] > righthalf[j][len(righthalf[j]) - 1]:
            return True
        return False
    else:
        if lefthalf[i][0] < righthalf[j][0]:
            return True
        return False
def makeWord(word,i):
    """
                            This function makes word
                            :param word: word
                            :param i: index
                            :return: None
                            :raises: None
                            :precondition: valid parameters
                            :complexity: best and worst case is O(1)
                            :postcondition: word made
                            """
    return '{}.{}'.format(word[:i], word[i + 1:])
def construct_word_graph(filename):
    """
                            This function creates the graph as an adjacency list
                            :param filename: name of file to be read
                            :return: None
                            :raises: None
                            :precondition: valid parameters
                            :complexity: best and worst case is O(n*m) where n is the number of words and m is the length of each word
                            :postcondition: graph created
                            """
    file = open(filename, 'r')
    array = []

    for item in file:
        array.append(item.strip('\n'))
    buckets = {}    # creating dictionary as a list.
    dict = {}

    for word in array:
        for i in range(len(word)):
            buckets[makeWord(word,i)] = set([])     # inserting the buckets inside the dictionary


    for word in array:
        for i in range(len(word)):
            buckets[makeWord(word,i)].add(word)

    for word in array:
        x = set([])
        for i in range(len(word)):
            x = x.union(buckets[makeWord(word,i)])
        x.remove(word)
        dict[word] = x

    return dict
def connected_components(graph):
    """
                            This function finds the connected components
                            :param graph: word graph
                            :return: connected components
                            :raises: None
                            :precondition: valid parameters
                            :complexity: best and worst case is O(|V| + |E|) where |V| is the number of vertices and |E| is the number of edges
                            :postcondition: components returned
                            """
    visited = {}
    for key in graph:
        visited[key] = False

    count = -1
    components = []
    temp = []

    for key in graph:
        if visited[key] == False:
            count += 1
            queue = Circular_Queue()
            queue.append(key)
            temp.append((key, count))
            visited[key] = True
        while not queue.is_empty():
            x = queue.serve()
            neighbours = graph[x]
            for item in neighbours:
                if visited[item] == False:
                    queue.append(item)
                    temp.append((item, count))
                    visited[item] = True

        if temp!= []:
            components.append(temp)
            temp = []


    return components
def find_diameter(word_graph, source):
    """
                            This function finds the diameter of a specific vertex
                            :param word_graph: graph of words
                            :param source: vertex of which the diameter is to be found
                            :return: None
                            :raises: None
                            :precondition: valid parameters
                            :complexity: best and worst case is O(|V| + |E|) where |V| is the number of vertices and |E| is the number of edges
                            :postcondition: diameter returned
                            """
    dist = {}
    visited = {}
    for item in word_graph:
        dist[item] = float("inf")
        visited[item] = False

    dist[source] = 0
    max = 0
    visited[source] = True
    q= Circular_Queue()
    q.append(source)

    while not q.is_empty():
        x = q.serve()
        neigbours = word_graph[x]
        for item in neigbours:
            if visited[item] == False:
                dist[item] = dist[x] + 1
                if max < dist[item]:
                    max = dist[item]
                q.append(item)
                visited[item] = True
    return max
def write_to_file(filename,array):
    """
                                This function writes to the file
                                :param filename: which file to write
                                :param array: contents to write
                                :return: None
                                :raises: None
                                :precondition: valid parameters
                                :complexity: best case is O(N) where N is the number of components and worst case is O(N*M) where N is the number of components and M is the number of vertics in the compoents
                                :postcondition: file written to
                                """

    file = open(filename,'w')
    for item in array:
        file.write('--- Component = ' + str(item[0][1]) + ' nVertices = ' + str(len(item)-1) + ' Diameter = ' + str(item[len(item)-1]) + '\n')
        for i in range (len(item)-1):
            file.write(item[i][0] + '\n')
        file.write('\n')
def main(inputfilename,outputfilename):
    """
                                This function finds the diameter of a specific vertex
                                :param inputfilename: file to read
                                :param outputfilename: file to write to
                                :return: None
                                :raises: None
                                :precondition: valid parameters
                                :complexity: best and worst case is O(|V|(|V| + |E|)) where |V| is the number of vertices and |E| is the number of edges
                                :postcondition: DONE
                                """
    graph = construct_word_graph(inputfilename)
    components = connected_components(graph)

    for i in range(len(components)):
        components[i] = mergeSort(components[i], 2)

    for item in components:
        max = float('-inf')
        for key in item:
            diameter = find_diameter(graph, key[0])
            if max < diameter:
                max = diameter
        item.append(max)

    write_to_file(outputfilename, mergeSort(components, 1))


if __name__ == '__main__':
    starts = timeit.default_timer()
    main('words5letter.txt','sample_task2_output.txt')
    taken = (timeit.default_timer() - starts)
    print(taken)


