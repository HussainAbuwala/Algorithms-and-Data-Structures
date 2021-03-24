class union_by_rank:
    '''

    description:            - disjoint data structure of N elements is initialised
    param: N                - Number of elements in the disjoint set
    return:                 - disjoint set

    '''

    def __init__(self,N):

        self.parent = [0] * N
        for i in range(N):
            self.make_disjoint_set(i)

    '''

    description:            - parent array is initialised with -1
    param: x                - x'th element in the parent array to be initialised
    return:                 - None

    '''
    def make_disjoint_set(self,x):

        self.parent[x] = -1


    def is_all_in_one_set(self):
        for i in range(len(self.count)):
            if(self.count[i] == len(self.count)):
                return True

        return False


    '''

    description:            - leader of the tree is found and returned. Along the way, path compression is also performed
    param: a                - element of which the leader is to be found out
    return:                 - leader of the tree in which 'a' belongs

    '''
    def find(self,a):

        #find root/leader of the tree containing 'a'

        if(self.parent[a] < 0):
            return a
        else:
            self.parent[a] = self.find(self.parent[a])
            return self.parent[a]

    '''

    description:            - an union by height is performed among two elements 'a' and 'b'
    param: a                - element
    param: b                - element
    return:                 - None

    '''
    def union(self,a,b):

        root_a = self.find(a)
        root_b = self.find(b)

        if(root_a == root_b):
            return

        height_a = -1 * self.parent[root_a]
        height_b = -1 * self.parent[root_b]

        if(height_a > height_b):
            self.parent[root_b] = root_a

        elif (height_b > height_a):
            self.parent[root_a] = root_b

        else:
            self.parent[root_a] = root_b
            self.parent[root_b] = -1 * (height_b + 1)

