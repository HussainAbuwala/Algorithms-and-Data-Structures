class union_find:

    def __init__(self,N):

        self.subsets = [None] * N
        self.subset_size = [None] * N
        self.initialise()

    def initialise(self):
        for i in range(len(self.subsets)):  # takes O(N)
            self.subsets[i] = i
            self.subset_size[i] = 1

    def find_root(self,x):

        y = x
        while  self.subsets[y] != y:            #takes O(lg*N), in practical it is almost constant time

                y = self.subsets[y]

        self.subsets[x] = y
        return y

    def find_which_subset_is_smaller(self,a,b):
        return self.subset_size[a] < self.subset_size[b]  #constant time


    def union(self,x,y):                        #takes O(lg*N), in practical it is almost constant time

        root_x = self.find_root(x)
        root_y = self.find_root(y)

        if self.find_which_subset_is_smaller(root_x,root_y):
            self.subsets[root_x] = self.subsets[root_y]
            self.subset_size[root_y]+= self.subset_size[root_x]
            return
        self.subsets[root_y] = self.subsets[root_x]
        self.subset_size[root_x] += self.subset_size[root_y]

    def find(self,x,y):                              #takes O(lg*N), in practical it is almost constant time
        root_x = self.find_root(x)
        root_y = self.find_root(y)

        return root_x == root_y


if __name__ == '__main__':
    myDisjoint = union_find(4)
    myDisjoint.union(1,2)
    print(myDisjoint.subsets)
    myDisjoint.union(0,3)
    print(myDisjoint.subsets)
    myDisjoint.union(1,0)
    print(myDisjoint.subsets)
    print(myDisjoint.find_root(3))
    print(myDisjoint.subsets)








