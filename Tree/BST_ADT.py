from BST_Node import Node
from circular_queue import Circular_Queue

class BST:

    def __init__(self):
        self.root = None
        self.count = 0


    def is_empty(self):
        if self.root == None and self.count == 0:
            return True
        else:
            return False

    def is_full(self):
        return False

    def __len__(self):
        return self.count

    def insert(self,item):

        if self.count == 0:
            new_node = Node(item, None, None)
            self.root = new_node
            self.count+=1


        else:
            temp_root = self.root
            self._insert_node(item,temp_root)


    def _insert_node(self,item,temp_root):

        if  temp_root == None:
            new_node = Node(item,None,None)
            self.count+=1
            return new_node

        elif item <= temp_root.item:
            temp_root.left_child = self._insert_node(item,temp_root.left_child)
            return temp_root
        else:
            temp_root.right_child = self._insert_node(item,temp_root.right_child)
            return temp_root

    def search(self,item):

        if self.root == None and self.count == 0:
            return False

        else:
            temp_root = self.root
            return self._search(item,temp_root)

    def _search(self,item,temp_root):

        try:
            if temp_root.item == item:
                return True

            elif item <= temp_root.item:
                return self._search(item,temp_root.left_child)
            else:
                return self._search(item,temp_root.right_child)

        except AttributeError:
            return False


if __name__ == '__main__':
    tree = BST()
    tree.insert(25)
    tree.insert(20)
    tree.insert(30)
    tree.insert(18)
    tree.insert(40)
    tree.insert(28)
    tree.insert(29)
    tree.insert(5)
    tree.insert(100)
    tree.queue.print_queue()