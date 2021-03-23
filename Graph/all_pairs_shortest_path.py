def floyd_warshalls_all_pairs(graph):


    for k in range(len(graph)):                 #try all intermediate vertices
        for i in range(len(graph)):             #source
            for j in range(len(graph)):         #destination
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
        print(graph)

    #If two vertices are directly connected, thats great, they will have some weight. If we can reach some vertice by adding
    # atleast one intermediate vertice, we can check if adding a new vertice improve our distance estimate.
    #If not, we keep the previous estimate.

    return graph

if __name__ == '__main__':
    graph = [[0,-5],[-10,0]]

    print(floyd_warshalls_all_pairs(graph))