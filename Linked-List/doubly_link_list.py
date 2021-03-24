from NODE_DOUBLE import Node

class LinkedList:

    def __init__(self):
        self.head = None
        self.count = 0

    def is_empty(self):
        if self.head == None and self.count == 0:
            return True
        else:
            return False

    def is_full(self):
        return False

    def __len__(self):
        return self.count

    def append(self,item):
        if self.is_empty() == True:
            new_node = Node(item, None,None)
            self.head = new_node
            self.count += 1
        else:
            node = self._get_node(self.count-1)
            new_node = Node(item, node.next,node)
            node.next = new_node
            self.count += 1

    def _get_node(self,index):
        if index <0 or index >=self.count:
            raise IndexError

        node = self.head

        for _ in range(index):
            node = node.next

        return node

    def insert(self,index,item):
        if index <0:
            index = -1 * index
            index = self.count - index

        if  (self.is_empty() == True and (index == self.count or index == -1)):
            self.append(item)
        elif index == 0:
            new_node = Node(item, self.head,None)
            self.head.previous = new_node
            self.head = new_node
            self.count+= 1
        else:
            node = self._get_node(index-1)
            if node.next == None:
                self.append(item)
            else:
                new_node = Node(item, node.next,node)
                new_node.next.previous = new_node
                node.next = new_node
                self.count+= 1

    def delete(self,index):
        if index <0:
            index = -1 * index
            index = self.count - index

        if  (index == self.count) or (self.count == 0):
            raise IndexError

        elif index == 0 and self.count == 1:
            self.head = None
            self.count-=1

        elif index == 0:
            self.head.next.previous = None
            self.head = self.head.next
            self.count -= 1
        else:
            node = self._get_node(index - 1)
            if node.next.next == None:
                node.next = None
                self.count -=1
            else:
                node.next.next.previous = node
                node.next = node.next.next
                self.count -= 1

    def remove(self,item):

        front = self.head
        check = False
        for i in range (self.count):
            if front.item == item:
                check = True
                save = i
                break
            front = front.next

        if check == False:
            raise ValueError

        self.delete(save)

    def __str__(self):
        if self.is_empty():
            return '" "'

        front = self.head
        string = ''
        for _ in range(self.count):
            string += str(front.item) + '\n'
            front = front.next

        return string

    def reset(self):
        self.head = None
        self.count = 0

def read_file(linklist,filename):
    """
    This function reads line into the list from the file
    :param alist: List ADT
    :param filename: name of the file from which to read lines
    :return:True or False depending on if the file is found or not
    :raises: Assertion error if filename is not a string and FileNotFoundError if file is not found
    :precondition: list and valid filename is entered which exits
    :complexity: best and worst case is O(n) where n is the number of lines in the list
    :postcondition: All the lines of a file are read into the list line by line
    """
    assert isinstance(filename, str), 'Filename should be a string'

    try:
        file = open(filename, 'r')
        for line in file:
            linklist.append((line).strip("\n"))

        file.close()
    except FileNotFoundError:
        return False

    return True

if __name__ == '__main__':
    link_list = LinkedList()
    link_list.append(1)
    link_list.append(3)
    link_list.append(3)
    link_list.remove(3)
    print(link_list)