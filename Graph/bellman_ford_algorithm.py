def bellman_ford(graph,source = 0):

    dist = [float('inf')] * len(graph)
    dist[source] = 0
    edge_list = []

    for i in range(len(graph)):
        for j in range(len(graph)):
            if graph[i][j] != 0:
                edge_list.append((i,j,graph[i][j]))

    no_of_vertice = len(graph)
    for _ in range(no_of_vertice-1):                              #|V| times iterations
        for edges in edge_list:                                 #|E| times iterations
            if dist[edges[1]] > dist[edges[0]] + edges[2]:
                dist[edges[1]] = dist[edges[0]] + edges[2]

    for edges in edge_list:
        if dist[edges[1]] > dist[edges[0]] + edges[2]:
            print('NEGATIVE WEIGHTED CYCLE DETECTED')
            return

    print(dist)

    #time complexity is | V | | E |
    #for sparse graphs, | V | ^ 2
    #for dense graphs, | V | ^ 3


if __name__ == '__main__':
    graph = [[0, 5,0],
        [0,0,-5],
        [0,-10,0]]

    bellman_ford(graph,0)