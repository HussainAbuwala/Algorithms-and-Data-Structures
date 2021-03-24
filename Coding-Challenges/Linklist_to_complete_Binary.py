from circular_queue import Circular_Queue
from BinaryTreeNode import BinaryTreeNode
from my_linked_list import List

def linklist_to_complete_binary_tree(head):

    count = 1
    current = head
    root = BinaryTreeNode(head.item)
    queue = Circular_Queue()
    queue.append(root)

    while queue.is_empty()!=True:

        temp = queue.serve()
        left,right = find(current,count)

        if left != None and right != None:
            temp.left = BinaryTreeNode(left.item)
            temp.right = BinaryTreeNode(right.item)
        elif left!=None:
            temp.left = BinaryTreeNode(left.item)

        current = current.next
        count+= 1

        if temp.left != None and temp.right!= None:
            queue.append(temp.left)
            queue.append(temp.right)
        elif temp.left!= None:
            queue.append(temp.left)

    return root


def find(current,count):
    left = 2*count
    right = 2*count+1

    while current!=None and count!=left:
        current = current.next
        count+=1

    if current!=None:
        temp = current.next
        return current,temp
    return None,None

def level_order_traversal(root):

    queue = Circular_Queue()

    queue.append(root)

    while queue.is_empty()!=True:
        node = queue.serve()
        print(node.item,)

        if node.left!=None:
            queue.append(node.left)
        if node.right!=None:
            queue.append(node.right)


def _print_inorder_aux_(copy):
    if copy == None:
        return
    else:
        _print_inorder_aux_(copy.left)
        print(copy.item)
        _print_inorder_aux_(copy.right)



if __name__ == '__main__':
    linklist = List()
    linklist.insert(0,10)
    linklist.insert(1,12)
    linklist.insert(2,15)
    linklist.insert(3,25)
    linklist.insert(4,30)
    linklist.insert(5,36)

    root = linklist_to_complete_binary_tree(linklist.head)
    level_order_traversal(root)
    #_print_inorder_aux_(root)
