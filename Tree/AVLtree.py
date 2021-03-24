from AvlNode import AVLnode

class AVLtree:

    def __init__(self):
        self.root = None

    def insert(self,key):
        if self.root == None:
            self.root = AVLnode(key)
        else:
            trav = self.root
            self.root = self._aux_insert(key,trav)


    def _aux_insert(self,key,trav):
        if trav == None:
            return AVLnode(key)
        elif (key < trav.item):
            trav.left = self._aux_insert(key,trav.left)
            self.updateHeights(trav)
            if self.find_balance_factor(trav) < -1 or self.find_balance_factor(trav) > 1:
                trav = self.rebalance(trav)
            return trav
        else:
            trav.right = self._aux_insert(key,trav.right)
            self.updateHeights(trav)
            if self.find_balance_factor(trav) < -1 or self.find_balance_factor(trav) > 1:
                trav = self.rebalance(trav)
            return trav

    def rebalance(self,node):

        if self.find_balance_factor(node) < 0:
            rightnode = node.right
            if self.find_balance_factor(rightnode) < 0:
                return self.rotate_left_left(node)
            else:
                node.right = self.rotate_right_right(node.right)
                return self.rotate_left_left(node)
        else:
            leftnode = node.left
            if self.find_balance_factor(leftnode) > 0:
                return self.rotate_right_right(node)
            else:
                node.left = self.rotate_left_left(node.left)
                return self.rotate_right_right(node)

    def rotate_left_left(self,node):
        root = node.right
        node.right = root.left
        root.left = node
        self.updateHeights(node)
        self.updateHeights(root)
        return root

    def rotate_right_right(self,node):
        root = node.left
        node.left = root.right
        root.right = node
        self.updateHeights(node)
        self.updateHeights(root)
        return root



    def updateHeights(self,node):

        if (node.left == None) and (node.right!=None):
            node.height = 1 + max(-1, node.right.height)
        elif (node.right == None) and (node.left!=None):
            node.height = 1 + max(node.left.height, -1)
        elif (node.left == None) and (node.right == None):
            node.height = 1 + max(-1,-1)
        else:
            node.height = 1 + max(node.left.height,node.right.height)

    def find_balance_factor(self,node):

        if (node.left == None) and (node.right!=None):
            return (-1 - node.right.height)
        elif (node.right == None) and (node.left!=None):
            return (node.left.height - (-1))
        else:
            return (node.left.height - node.right.height)


tree = AVLtree()
tree.insert(19)
tree.insert(23)
tree.insert(13)
tree.insert(7)
tree.insert(73)
tree.insert(3)
tree.insert(18)
tree.insert(17)
tree.insert(11)

print(tree.root.item)
print(tree.root.left.item)
print(tree.root.right.item)

