from circular_queue import Circular_Queue
from Stack_ADT import Stack

def reverse_k(a_queue,k):

    if k == 0:
        return a_queue

    stack = Stack()
    new_queue = Circular_Queue()

    i = 0
    while a_queue.is_empty() == False and i!=k:
        stack.push(a_queue.serve())
        i+=1

    while a_queue.is_empty() == False:
        new_queue.append(a_queue.serve())

    while stack.is_empty()== False:
        a_queue.append(stack.pop())

    while new_queue.is_empty() == False:
        a_queue.append(new_queue.serve())

    return a_queue

class PositiveIterator:
    def __init__(self,the_list):
        self.array = the_list
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):

        while self.count < len(self.array):
            if self.array[self.count] > 0:
                self.count += 1
                return self.array[self.count-1]
            self.count+=1

        raise StopIteration

class PrimeIterator:
    def __init__(self,n):
        self.start = n

    def __iter__(self):
        return self

    def __next__(self):
        while True:

            check = False
            for i in range (self.start-1,1,-1):
                if self.start%i == 0:
                    check = True
                    break

            if check == True:
                self.start+=1
            else:
                self.start+=1
                return self.start-1





if __name__ == '__main__':
    prime = PrimeIterator(3)
    prim = iter(prime)
    print(next(prim))
    print(next(prim))
    print(next(prim))
    print(next(prim))
    print(next(prim))
    print(next(prim))
    print(next(prim))

