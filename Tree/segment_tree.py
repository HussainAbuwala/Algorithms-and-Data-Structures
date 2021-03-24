class Segment_tree:
    def __init__(self,size=100):
        self.seg = [None] * size
        self.array = []
        self.count = 0

    def construct_tree(self,user_array,lo,hi,pos):
        if lo == hi:
            self.seg[pos] = user_array[lo]
            return user_array[lo]
        else:
            mid = (lo + hi) //2
            min_left = self.construct_tree(user_array,lo,mid,2*pos)
            min_right = self.construct_tree(user_array,mid+1,hi,2*pos + 1)
            self.seg[pos] = min(min_left,min_right)
            return min(min_left,min_right)

    def construct_indexes(self):

        self.array = self._aux_construct_index(1)

    def _aux_construct_index(self,k):

        if (self.seg[k] == None):
            return None
        else:
            left = self._aux_construct_index(2*k)
            right = self._aux_construct_index(2*k+1)
            if left == None and right == None:
                return [k]
            return left + right

    def query(self,user_lo,user_hi,length):

        return self._aux_query_(1,0,length-1,user_lo,user_hi)

    def _aux_query_(self,k,lo,hi,user_lo,user_hi):

        if (lo >= user_lo and lo <= user_hi) and (hi >= user_lo and hi <= user_hi):
            return self.seg[k]
        elif (lo < user_lo or lo > user_hi) and (hi < user_lo or hi > user_hi):
            return None
        else:
            mid = lo + hi // 2
            min_left = self._aux_query_(2*k,lo,mid,user_lo,user_hi)
            min_right = self._aux_query_(2*k+1,mid+1,hi,user_lo,user_hi)
            if min_left == None:
                return min_right
            elif min_right == None:
                return min_left
            return min(min_left,min_right)

    def update(self,k,val):

        temp = self.array[k]

        self.seg[temp] = val

        self.rise(temp)

    def rise(self,temp):

        while self.seg[temp//2] != None:
            parent = temp//2
            left = 2* parent
            right = 2*parent + 1

            if (min(self.seg[left],self.seg[right])) != (self.seg[parent]):
                self.seg[parent] = min(self.seg[left],self.seg[right])
                temp = parent
            else:
                break






def get_min_range(arr,lo,hi):

    seg_heap = Segment_tree()
    seg_heap.construct_tree(arr,0,len(arr)-1,1)
    return seg_heap.query(lo,hi,len(arr))

if __name__ == '__main__':
    arr = [1,2,3,4]
    seg_heap = Segment_tree()
    seg_heap.construct_tree(arr, 0, len(arr) - 1, 1)
    seg_heap.construct_indexes()
    print(seg_heap.query(0,3,4))
    seg_heap.update(3,0)
    print(seg_heap.query(0,3,4))
    seg_heap.update(1,-1)
    print(seg_heap.query(0,3,4))

