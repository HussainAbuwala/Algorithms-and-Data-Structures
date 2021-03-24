class Queue:

    def __init__(self,size=100):
        assert size >0, "Size should be positive"
        self.array = size * [None]
        self.count = 0
        self.front = 0
        self.rear = 0

    def is_empty(self):
        return self.count == 0

    def is_full(self):
        return self.rear >= len(self.array)

    def reset(self):
        self.count = 0
        self.front = 0
        self.rear = 0

    def append(self,item):
        assert not self.is_full(),"Queue is full"
        self.array[self.rear] = item
        self.rear += 1
        self.count += 1

    def serve(self):
        assert not self.is_empty(), "Queue is empty"
        item = self.array[self.front]
        self.front += 1
        self.count -= 1
        return item

    def print_queue(self):
        assert not self.is_empty(), "Queue is empty"
        front = self.front

        while front<self.rear:
            print(str(self.array[front]))
            front += 1


if __name__ == '__main__':
    queue = Queue(3)
    queue.append(1)
    queue.append(2)
    queue.append(3)
    queue.serve()
    queue.append(4)
    queue.print_queue()



