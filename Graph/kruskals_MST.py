from own_heap import  myHeap
from union_find_rank_path_compression import union_find

def kruskalks_mst(graph):


    priority_queue = myHeap()

    for i,item in enumerate(graph):
        for j,item1 in enumerate(item):
            if graph[i][j] > 0:
                priority_queue.add(graph[i][j],(i,j))


    #First i added |E| edges with their weight as key into the min_heap. So building the min_heap is O(|E|log|E|)
    my_disjoint_set = union_find(len(graph))    #initialising the disjoint_set is O(|V|)
    holding_MST = []

    while priority_queue.isEmpty() == False:                #O(E)

        minimum_edge = priority_queue.extract_min()[1]           #O(LOG|E|)
        if my_disjoint_set.find(minimum_edge[0],minimum_edge[1]) == False: #O(log * |V|) #using path compression and union by size
            holding_MST.append(minimum_edge)
            my_disjoint_set.union(minimum_edge[0],minimum_edge[1]) #O(log * |V|) #using path compression and union by size

    #So the total time complexity is  O(|E|log|E|) + O(|V|) + O(|E|LOG|E|) + O(|E|LOG * |V|) + O(|E|LOG * |V|)

    #So

    return holding_MST



if __name__ == '__main__':
    graph = [[0, 2, 0, 6, 0],
            [2, 0, 3, 8, 5],
            [0, 3, 0, 0, 7],
            [6, 8, 0, 0, 9],
            [0, 5, 7, 9, 0]]

    print(kruskalks_mst(graph))