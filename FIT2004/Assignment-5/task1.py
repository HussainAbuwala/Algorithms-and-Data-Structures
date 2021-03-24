def write_to_file(filename,string):
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
    file.write(string)

def construct_d_graph(array):
    """
                                    This function creates the graph
                                    :param array: words
                                    :return: adj_list
                                    :raises: None
                                    :precondition: valid parameters
                                    :complexity: best case is O(N) where N is the number of words
                                    :postcondition: graph constructed
                                    """

    buckets = {}  # creating dictionary as a list.
    edge_list = [[] for _ in range(len(array))]


    for word in array:
        for i in range(2):
            if i == 1:
                buckets[word[1:]] = []
            else:
                buckets[word[:len(word)-1]] = []

    for index, word in enumerate(array):
        for i in range(1):
            buckets[word[:len(word)-1]].append(index)


    for i, word in enumerate(array):
        x = buckets[word[1:]]
        for item in x:
            edge_list[i].append((i,item))

    return edge_list

def construct_words(words,string,n,array):
    """
                                    This function constructs the words
                                    :param words: words
                                    :param string: temp
                                    :param n: length of string
                                    :param array: array to store each word
                                    :return: array
                                    :raises: None
                                    :precondition: valid parameters
                                    :complexity:  best and worst case is 2^N where n is the number of words
                                    :postcondition: array of words returned
                                    """


    if len((string)) == n:
        array.append(string)
        return array

    for item in words:
        array = construct_words(words,string + item,n,array)

    return array

def Hierholzer(edge_list,source):
    """
                                        This function finds the eulerian cycle
                                        :param edge_list: adj list
                                        :param source: vertice to start with
                                        :return: eulerian path
                                        :raises: None
                                        :precondition: valid parameters
                                        :complexity:  best and worst case is O(E) where E is the number of edges
                                        :postcondition: eulerian path found
                                        """
    
    first_circle = []

    while True:
        check = [None,False]
        sub_tour = source
        second_circle = find_path_to_source(source,source,edge_list,[source],check)
        first_circle = join_tour(first_circle,second_circle,sub_tour)
        if check[1] == False:
            break
        source = check[0]

    return first_circle

def join_tour(first_circle,second_circle,sub_tour):
    """
                                            This function finds joins to cycles on common vertice
                                            :param first_circle: main cycle
                                            :param second_circle: temp cycle
                                            :param sub_tour: vertice to start the temp cycle
                                            :return: joined path
                                            :raises: None
                                            :precondition: valid parameters
                                            :complexity:  best and worst case is O(v) where v is the number of vertices
                                            :postcondition: eulerian path found
                                            """

    temp = []
    i = 0

    while i < len(first_circle):
        if first_circle[i] == sub_tour:
            temp+= second_circle
            break
        temp.append(first_circle[i])
        i+=1

    if first_circle == []:
        return second_circle
    temp = temp + first_circle[i+1:]
    return temp

def find_path_to_source(source,vertice,edge_list,cycle,check):
    """
                                                This function finds path from one vertice to the same vertice
                                                :param source: vertice to start with
                                                :param vertice: temp vertice
                                                :param edge_list: adjlist
                                                :param cycle: list store the cycle
                                                :param check: to see if unvisited left
                                                :return: cycle
                                                :raises: None
                                                :precondition: valid parameters
                                                :complexity:  best and worst case is O(E) where E is the number of edges
                                                :postcondition: cycle found
                                                """
    edges = edge_list[vertice]
    temp = edges[len(edges)-1][1]
    cycle.append(temp)
    edges.pop()
    if edges!=[] and check[1] == False:
        check[0] = vertice
        check[1] = True
    if temp == source:
        return cycle
    return find_path_to_source(source,temp,edge_list,cycle,check)

def make_string(cycle,words):
    """
                                                    This function finds make the string
                                                    :param cycle: eulerian cycle
                                                    :param words: all words
                                                    :return: string
                                                    :raises: None
                                                    :precondition: valid parameters
                                                    :complexity:  best and worst case is O(E) where E is the number of edges
                                                    :postcondition: string made
                                                    """

    string = words[cycle[0]]

    for i in range(1,len(cycle)):
        temp = words[cycle[i]]
        string+= temp[len(temp)-1]

    return string

def main(m,n):

    """
    
    Everything is done from here
    
    :param m: number of letter
    :param n: length of string
    :return: None
    """

    alphabets = ['A','B','C','D','E','F','G','H','I','J','K','L','M']

    letters = []

    for i in range(m):
        letters.append(alphabets[i])


    words = construct_words(letters,'',n,[])
    adjlist = construct_d_graph(words)
    cycle = Hierholzer(adjlist,0)
    string = make_string(cycle,words)
    write_to_file('outputTask1.txt',string)


if __name__ == '__main__':
    m = int(input('m: '))
    n = int(input('n: '))
    assert (m >= 2 and m <= 5), "Please keep m between 2 and 5"
    assert (n >= 2 and n <= 3), "Please keep n between 2 and 3"
    main(m,n)