class Node:
    def __init__(self,item = None,link = None):
        self.item = item
        self.next = link

    def __str__(self):
        return self.item

if __name__ == '__main__':
    n4 = Node('Tasin')
    n1 = Node('Konrad',n4)
    n3 = Node('Omam',n1)
    n2 = Node('Hussain',n3)
    n5 = Node('Abrahim',n2)

    print(n4.next)