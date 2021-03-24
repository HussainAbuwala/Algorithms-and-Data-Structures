from BinarySearchTree import BinarySearchTreeNode

class AVLTREE:

    def __init__(self):
        self.root = None
        self.count = 0

    def __len__(self):
        return self.count

    def insert(self,key,value=None):

        if self.root == None:
            self.root = BinarySearchTreeNode(key,value)
        else:
            current = self.root
            self.aux_insert(current,current,key,value)

        self.count+=1

    def aux_insert(self,parent,current,key,value):

        if current == None:
            return BinarySearchTreeNode(key,value)
        elif key < current.key:
            current.left = self.aux_insert(current,current.left,key,value)
            cal = self.find_diff(current,current)
            if cal >1 or cal <-1:
                current = self.control_center(parent,current,cal)
            return current
        else:
            current.right = self.aux_insert(current,current.right, key, value)
            cal = self.find_diff(current, current)
            if cal > 1 or cal < -1:
                current = self.control_center(parent, current, cal)
            return current

    def control_center(self,parent,current,cal):
        if cal > 1:

            cal2 = self.find_diff(current.left,current.left)
            if cal2 > 0 or cal2 == 0:
                return self.right_rotation(parent,current,current.left)
            elif cal2 <0:
                self.left_rotation(current,current.left,current.left.right)
                return self.right_rotation(parent,current,current.left)

        elif cal < -1:

            cal2 = self.find_diff(current.right,current.right)
            if cal2 < 0 or cal2 == 0:
                return self.left_rotation(parent,current,current.right)
            elif cal2 >0:
                self.right_rotation(current,current.right,current.right.left)
                return self.left_rotation(parent,current,current.right)

    def left_rotation(self,parent,current,child):

        save = child.left
        child.left = current
        current.right = save

        if parent == current:
            self.root = child
        elif parent.left == current:
            parent.left = child
        else:
            parent.right = child

        return child

    def right_rotation(self,parent,current,child):

        save = child.right
        child.right = current
        current.left = save

        if parent == current:
            self.root = child
        elif parent.left == current:
            parent.left = child
        else:
            parent.right = child

        return child

    def find_diff(self,root,current):
        if current == None:
            return -1
        else:
            height_left = 1 + self.find_diff(root,current.left)
            height_right = 1 + self.find_diff(root,current.right)
            if current == root:
                return height_left - height_right
            return max(height_left,height_right)

def avlsort(root):
    _print_inorder_aux_(root)

def _print_inorder_aux_(copy):

    if copy == None:
        return
    else:
        _print_inorder_aux_(copy.left)
        print(copy.key)
        _print_inorder_aux_(copy.right)





if __name__ == '__main__':
    bst = AVLTREE()
    bst.insert(10)
    bst.insert(80)
    bst.insert(60)
    bst.insert(4400)
    bst.insert(32)
    bst.insert(87)
    bst.insert(321)
    avlsort(bst.root)



