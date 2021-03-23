from own_heap import myHeap
def find_min(array,dist):
    min = float('inf')
    min_vertice = None

    for item in array:
        if dist[item] < min:
            min = dist[item]
            min_vertice = item

    for item in array:
        if item == min_vertice:
            array.remove(item)
            break

    return min_vertice,min


def naive_dijkstras(graph,source):

    adj_list = {}
    dist ={}
    remaining_set = []
    removed_set = []
    source = source

    for i in range(len(graph)):
        adj_list[i] = []
        dist[i] = float('inf')
        remaining_set.append(i)
        for j in range(len(graph)):
            if graph[i][j] > 0:
                x = adj_list[i]
                x.append(j)

    dist[source] = 0


    while remaining_set != []:                                                                                  #takes |V| operations
        min_vertice,min_dist = find_min(remaining_set,dist)                                                     #|V| operations
        removed_set.append((min_vertice,min_dist))                                                              #constant time
        for neighbours in adj_list[min_vertice]:                                                                #|E| operations in total
            if dist[min_vertice] + graph[min_vertice][neighbours] < dist[neighbours]:                           #constant time
                dist[neighbours] = dist[min_vertice] + graph[min_vertice][neighbours]                           #constant time updation

    #Using an array as a queue, total time take is |V|*|V| + |E|*1 = |V|^2 + |E|
    #For sparse graphs, time complexity is |V|^2 + |V| = |V|^2
    #For dense graphs, time complexity is |V|^2 + |V|^2 = 2|V|^2

    return removed_set


def efficient_dijkstras(graph,source = 0):

    adj_list = [None] * len(graph)
    dist = [(float('inf'),False)] * len(graph)
    predecessor = [None] * len(graph)
    dist[source] = (0,False)
    dijkstra_heap = myHeap()

    for i in range(len(graph)):
        adj_list[i] = []
        if i==source:
            dijkstra_heap.add(0,i)
        else:
            dijkstra_heap.add(float('inf'),i)

        for j in range(len(graph)):
            adlist = adj_list[i]
            if graph[i][j] > 0:
                adlist.append(j)

    removed_set = []


    while  dijkstra_heap.isEmpty() == False:            #runs |V| times
        finalised = dijkstra_heap.extract_min()         #|log|V|| times
        if dist[finalised[1]][1] == True:
            continue
        else:
            dist[finalised[1]] = (finalised[0],True)
            removed_set.append(finalised)

        for item in adj_list[finalised[1]]:             #runs |E| times
            if dist[finalised[1]][0] + graph[finalised[1]][item] < dist[item][0]:                           #constant time
                dist[item] = (dist[finalised[1]][0] + graph[finalised[1]][item],False)
                predecessor[item] = finalised[1]
                dijkstra_heap.add(dist[item][0],item)   #log|v| times


    #total time = |V|log|V| + |E|log|V|
    #for sparse graphs, |V|log|V| + |V|log|V| = 2Vlog|V|
    #for dense graphs, |V|log|V| + |V|^2log|V|


    return predecessor







if __name__ == '__main__':
    graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
             [4, 0, 8, 0, 0, 0, 0, 11, 0],
             [0, 8, 0, 7, 0, 4, 0, 0, 2],
             [0, 0, 7, 0, 9, 14, 0, 0, 0],
             [0, 0, 0, 9, 0, 10, 0, 0, 0],
             [0, 0, 4, 14, 10, 0, 2, 0, 0],
             [0, 0, 0, 0, 0, 2, 0, 1, 6],
             [8, 11, 0, 0, 0, 0, 1, 0, 7],
             [0, 0, 2, 0, 0, 0, 6, 7, 0]
             ]
    print(efficient_dijkstras(graph))
    print(naive_dijkstras(graph,0))


