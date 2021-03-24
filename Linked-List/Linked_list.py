from Node import Node

class Linked_List:

    def __init__(self):
        self.head = None
        self.fixed = None
        self.count = 0

    def is_full(self):
        return False

    def is_empty(self):
        if self.head == None and self.count == 0 and self.fixed == None:
            return True
        else:
            return False

    def __len__(self):
        return self.count

    def __contains__(self, item):
        if self.is_empty() == True:
            return False
        else:
            found = False
            front = self.fixed
            for i in range(self.count):
                if front.item == item:
                    found = True
                    break
                front = front.next
            return found

    def append(self,item):
        new_node = Node(item,None)
        if self.is_empty() == True:
            self.head = new_node
            self.fixed = new_node
            self.count += 1
        else:
            self.head.next = new_node
            self.head = new_node
            self.count += 1

    def _get_node(self,index):
        if index <0 or index>= self.count:
            raise IndexError

        front = self.fixed
        for _ in range(index):
            front = front.next

        return front

    def delete(self,index):
        assert not self.is_empty(),'cannot delete from empty list'

        if index == self.count:
            raise IndexError

        elif index == 0 and self.count == 1:
            self.fixed = None
            self.head = None
            self.count -= 1
        elif index == 0:
            self.fixed = self.fixed.next
            self.count -= 1
        else:
            node = self._get_node(index-1)

            node.next = node.next.next
            if node.next == None:
                self.head = node
                self.count -=1
            else:
                self.count-= 1

    def insert(self,index,item):
        if (self.is_empty()  == True and index ==0) or index == self.count:
            self.append(item)

        elif index == 0:
            new_node = Node(item,None)
            new_node.next = self.fixed
            self.fixed = new_node
            self.count += 1

        else:
            new_node = Node(item,None)
            node = self._get_node(index-1)
            new_node.next = node.next
            node.next = new_node
            self.count += 1

    def remove(self,item):
        assert not self.is_empty(),'Cannot remove item from empty list'

        front = self.fixed
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

    def print_list(self):
        assert not self.is_empty(), "List is empty"
        front = self.head

        for _ in range(self.count):
            print(front.item)
            front = front.next

    def double_list(self):

        current = self.head

        while current!= None:
            current.next = Node(current.item,current.next)
            current = current.next.next

if __name__ == '__main__':
    link_list = Linked_List()
    link_list.append(3)
    link_list.append(2)
    link_list.append(5)
    link_list.print_list()
