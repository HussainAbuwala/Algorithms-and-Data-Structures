class MaxHeap:
    def __init__(self):
        self.array = [None]
        self.count = 0

    def __len__(self):
        return self.count

    def add(self,item):
        if (self.count+1) >= len(self.array):
            self.array.append(item)
        else:
            self.array[self.count+1] = item

        self.count+=1
        self.rise(self.count)

    def rise(self,k):
        while self.array[k//2]!= None:
            parent = k//2
            if self.array[k] > self.array[parent]:
                self.array[k],self.array[parent] = self.array[parent],self.array[k]
                k = parent
            else:
                break

    def get_max(self):
        assert self.count>0, "EMPTY HEAP"
        item = self.array[1]
        self.array[1], self.array[self.count] = self.array[self.count], self.array[1]
        self.count-= 1
        self.sink(1)
        return item

    def sink(self,k):
        while ((2*k) <= self.count) or (((2*k)+1) <= self.count):
            child = self.find_largest_child(k)
            if self.array[k] < self.array[child]:
                self.array[k], self.array[child] = self.array[child], self.array[k]
                k = child
            else:
                break

    def find_largest_child(self,k):
        left = 2*k
        right = (2*k) + 1
        if (left<=self.count) and (right<=self.count):
            if self.array[left] > self.array[right]:
                return left
            else:
                return right
        else:
            return left

class MinHeap:

    def __init__(self):
        self.array = [None]
        self.count = 0

    def __len__(self):
        return self.count

    def add(self,item):
        if (self.count+1) >= len(self.array):
            self.array.append(item)
        else:
            self.array[self.count+1] = item

        self.count+=1
        self.rise(self.count)

    def rise(self,k):
        while self.array[k//2]!= None:
            parent = k//2
            if self.array[k] < self.array[parent]:
                self.array[k],self.array[parent] = self.array[parent],self.array[k]
                k = parent
            else:
                break

    def get_max(self):
        assert self.count>0, "EMPTY HEAP"
        item = self.array[1]
        self.array[1], self.array[self.count] = self.array[self.count], self.array[1]
        self.count-= 1
        self.sink(1)
        return item

    def sink(self,k):
        while ((2*k) <= self.count) or (((2*k)+1) <= self.count):
            child = self.find_largest_child(k)
            if self.array[k] > self.array[child]:
                self.array[k], self.array[child] = self.array[child], self.array[k]
                k = child
            else:
                break

    def find_largest_child(self,k):
        left = 2*k
        right = (2*k) + 1
        if (left<=self.count) and (right<=self.count):
            if self.array[left] < self.array[right]:
                return left
            else:
                return right
        else:
            return left



def heap_sort(the_list):

    heap = MinHeap()

    for item in the_list:           # n * logn
        heap.add(item)

    empty_list = [None] * len(the_list)

    for i in range (len(empty_list)):       # n * log n
        empty_list[i] = heap.get_max()      # worstcase(nlogn) and bestcase (nlogn)

    return empty_list


def is_valid_heap(array):
    for i in range(1, len(array)):
        check = check_child(i, len(array) - 1, array)
        if check == True:
            continue
        else:
            return False
    return True


def check_child(parent, count, array):
    left_child = 2 * parent
    right_child = (2 * parent) + 1

    if (left_child <= count) and (right_child <= count):
        if (array[parent] >= array[left_child]) and (array[parent] >= array[right_child]):
            return True
        else:
            return False
    elif (left_child <= count):
        if array[parent] >= array[left_child]:
            return True
        else:
            return False
    else:
        return True

def connect_n_ropes_min_cost(ropes_list):

    heap = MinHeap()

    for item in ropes_list:
        heap.add(item)

    mincost = 0

    while len(heap)!= 0:

        min_item = heap.get_max()
        if len(heap)!= 0:
            min_item2 = heap.get_max()
            total = min_item + min_item2
            mincost += total
            heap.add(total)

    return mincost



if __name__ == '__main__':
    print(heap_sort([100,4,3,2,1,-100,100,4,3,2,1,2,1]))
    #print(connect_n_ropes_min_cost([4,3,2]))







