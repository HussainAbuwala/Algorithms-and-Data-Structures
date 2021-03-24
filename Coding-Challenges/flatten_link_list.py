'''
Flattening a linked list
Given a linked list where every node represents a linked list and contains two pointers of its type:

Pointer to next node in the main list (we call it ‘right’ pointer in below code)
Pointer to a linked list where this node is head (we call it ‘down’ pointer in below code).
All linked lists are sorted. See the following example
5 → 10 → 19 → 28
↓        ↓        ↓          ↓
7       20     22       35
↓                  ↓         ↓
8                50      40
↓                             ↓
30                         45
Write a function flatten() to flatten the lists into a single linked list. The flattened linked list should also be sorted. For example, for the above input list, output list should be 5→7→8→10→19→20→22→28→30→35→40→45→50.
'''

class Node:
    def __init__(self,item = None,link = None,down=None):
        self.item = item
        self.next = link
        self.down = down


    def __str__(self):
        return self.item

class List:
    def __init__(self):
        self.head = None
        self.count = 0

    def is_empty(self):
        return self.count == 0

    def is_full(self):
        return False

    def reset(self):
        self.__init__()

    def __len__(self):
        return self.count

    def _get_node(self, index):
        assert 0 <= index < self.count, "Index out of bounds"
        node = self.head
        for _ in range(index):
            node = node.next
        return node


    def insert(self, index, item):
        if index < 0:
            index = 0
        elif index > len(self):
            index = len(self)
        if index == 0:
            self.head = Node(item, self.head)
        else:
            node = self._get_node(index-1)
            node.next = Node(item, node.next)
        self.count += 1

    def delete(self, index):
        if self.is_empty():
            raise IndexError("The list is empty")
        if index < 0 or index >= len(self):
            raise IndexError("Index is out of range")
        if index == 0:
            self.head = self.head.next
        else:
            node = self._get_node(index-1)
            node.next = node.next.next
        self.count -= 1

    def remove_duplicates(self):

        copy = self.head
        count = 0
        while copy != None:

            if copy.next != None and copy.item == copy.next.item:
                copy.next = copy.next.next

            copy = copy.next


def flatten(head):
    count = 0
    temp = head

    result = List()

    while temp!= None:

        if count==0:
            result = merge(temp,temp.down.head)
            count+=1
        else:
            result = merge(result.head,temp.down.head)
        temp = temp.next

    return result

def merge(Main_list_pointer,downlist):
    main_head = Main_list_pointer
    aux_head = downlist
    result = List()

    while (main_head != None) and (aux_head !=None):
        if main_head.item <= aux_head.item:
            result.insert(len(result),main_head.item)
            main_head = main_head.next

        else:
            result.insert(len(result),aux_head.item)
            aux_head = aux_head.next

    while main_head!=None:
        result.insert(len(result), main_head.item)
        main_head = main_head.next

    while aux_head!=None:
        result.insert(len(result), aux_head.item)
        aux_head = aux_head.next

    return result


def print_structure(node):
    current_node = node
    print("[", end="")
    while current_node is not None:
        print(current_node.item, end=", ")
        current_node = current_node.next
    print("]", end="")

if __name__ == '__main__':
    linklist = List()
    linklist.insert(0,7)
    linklist.insert(1,8)
    linklist.insert(2,30)

    linklist1 = List()
    linklist1.insert(0, 20)

    linklist2 = List()
    linklist2.insert(0,22)
    linklist2.insert(1,50)

    linklist3 = List()
    linklist3.insert(0,35)
    linklist3.insert(1,40)
    linklist3.insert(2,45)

    linklist4 = List()

    main_list= List()
    main_list.insert(0,5)
    main_list.insert(1,10)
    main_list.insert(2,19)
    main_list.insert(3,28)
    main_list.insert(4,29)

    main_list.head.down = linklist
    main_list.head.next.down = linklist1
    main_list.head.next.next.down = linklist2
    main_list.head.next.next.next.down = linklist3
    main_list.head.next.next.next.next.down = linklist4



    print_structure(flatten(main_list.head).head)









