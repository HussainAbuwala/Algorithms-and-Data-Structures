from Node import Node

class Linked_Queue:

    def __init__(self):
        self.front = None
        self.rear = None
        self.count = 0

    def is_empty(self):
        if self.front == None and self.rear == None:
            return True
        else:
            False

    def is_full(self):
        return False

    def reset(self):
        self.__init__()

    def __len__(self):
        return self.count

    def append(self,item):
        if self.is_empty() == True:
            new_node = Node(item,None)
            self.front = new_node
            self.rear = new_node
            self.count += 1
        else:
            new_node = Node(item,None)
            self.rear.next = new_node
            self.rear = new_node
            self.count += 1


    def serve(self):
        assert not self.is_empty(), "Queue is empty"
        item = self.front.item
        self.front = self.front.next
        if self.front == None:
            self.rear = None
        self.count -= 1
        return item

    def print_queue(self):
        assert not self.is_empty(), "Queue is empty"
        front = self.front

        for _ in range(self.count):
            print(front.item)
            front = front.next


if __name__ == '__main__':
    link_queue = Linked_Queue()
    link_queue.append(1)
    link_queue.append(2)
    link_queue.append(4)
    link_queue.serve()
    link_queue.serve()
    link_queue.serve()
    print(len(link_queue))