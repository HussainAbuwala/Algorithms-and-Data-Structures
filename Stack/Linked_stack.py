from Node import Node

class Linked_stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top == None

    def is_full(self):
        return False

    def reset(self):
        self.top = None

    def push(self,item):
        self.top = Node(item,self.top)

    def pop(self):
        assert not self.is_empty(), 'Stack is empty'
        item = self.top.item
        self.top = self.top.next
        return item

    def print_structure(self):
        assert not self.is_empty(), 'Stack is empty'
        node = self.top
        while node.next != None:
            print(node.item)
            node = node.next

        print(node.item)

if __name__ == '__main__':
    stack = Linked_stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.pop()
    stack.pop()
    stack.push(4)
    stack.push(10)
    stack.print_structure()
