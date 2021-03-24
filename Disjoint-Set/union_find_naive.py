class union_find:

    def __init__(self,N):

        self.array = [None] * N
        self.initialise()

    def initialise(self):

        for i in range(len(self.array)):  #takes O(N)
            self.array[i] = i

    def find(self,x,y):                         #takes O(1) time

        return self.array[x] == self.array[y]

    def union(self,x,y):                        #takes O(N) time

        temp = self.array[x]

        for i,item in enumerate(self.array):
            if item == temp:
                self.array[i] = self.array[y]




if __name__ == '__main__':
    disjoint = union_find(4)
    print(disjoint.find(1,2))
    disjoint.union(1,2)
    print(disjoint.find(1,2))
    print(disjoint.array)
    disjoint.union(1,3)
    print(disjoint.array)
    disjoint.union(3,0)
    print(disjoint.array)
    print(disjoint.find(1,2))
