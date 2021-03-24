from circular_queue import Circular_Queue
from Stack_ADT import Stack
class BinaryTreeNode:
    def __init__(self,item,left=None,right=None):
        self.item = item
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.item)


class BinaryTree:

    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root is None

    def add(self,item,position):

        if self.root == None:
            self.root = BinaryTreeNode(item)
            return
        string = iter(position)
        self.add_aux(self.root,string,item)
        return

    def add_aux(self,root,iterator,item):
        string = next(iterator)
        if string == '0':
            if root.left == None:
                root.left = BinaryTreeNode(item)
                return
            else:
                self.add_aux(root.left,iterator,item)
        elif string == '1':
            if root.right == None:
                root.right = BinaryTreeNode(item)
                return
            else:
                self.add_aux(root.right,iterator,item)



    '''def add(self,item,bitstring):

        if self.root == None and bitstring == '':
            new_node = BinaryTreeNode(item,None,None)
            self.root = new_node
            return True

        copy = self.root

        try:
            self._add_aux_(item,bitstring,copy)
            return True
        except AttributeError:
            return False

    def _add_aux_(self,item,bitstring,copy):

        if bitstring == '':
            new_node = BinaryTreeNode(item, None, None)
            return new_node
        elif bitstring[0] == '0':
            save = copy
            newnode = self._add_aux_(item,bitstring[1:],copy.left)
            if newnode != None:
                save.left = newnode
            return
        else:
            save = copy
            newnode = self._add_aux_(item, bitstring[1:], copy.right)
            if newnode!= None:
                save.right = newnode
            return'''

    def print_preorder(self):

        copy = self.root

        self._print_preorde_aux_(copy)



    def _print_preorde_aux_(self,copy):

        if copy == None:
            return
        else:
            print(copy.item)
            self._print_preorde_aux_(copy.left)
            self._print_preorde_aux_(copy.right)

    def print_inorder(self):

        copy = self.root

        self._print_inorder_aux_(copy)



    def _print_inorder_aux_(self,copy):

        if copy == None:
            return
        else:
            self._print_inorder_aux_(copy.left)
            print(copy.item)
            self._print_inorder_aux_(copy.right)

    def print_postorder(self):

        copy = self.root

        self._print_postorder_aux_(copy)



    def _print_postorder_aux_(self,copy):

        if copy == None:
            return
        else:
            self._print_postorder_aux_(copy.left)
            self._print_postorder_aux_(copy.right)
            print(copy.item)

    def find_path_max_sum(self):
        copy = self.root

        if copy == None:
            return 0

        sum = 0
        newlist = []
        newlist = self._find_path_max_sum_aux_(copy,sum,newlist)

        max = newlist[0]

        for item in newlist:
            if item> max:
                max = item

        return max


    def _find_path_max_sum_aux_(self,copy,sum,newlist):

        if copy == None:
            return
        else:
            sum += copy.item
            self._find_path_max_sum_aux_(copy.left,sum,newlist)
            self._find_path_max_sum_aux_(copy.right,sum,newlist)
            if copy.left == None and copy.right == None:
                newlist.append(sum)

        return newlist


def find_max_path(root):
    if root == None:
        return 0
    elif root.left == None and root.right == None:
        return root.item
    else:

        max = root.item + find_max_path(root.left)
        max2 = root.item + find_max_path(root.right)
        if max > max2 :
            return max
        else:
            return max2

def sum_total_nodes(root):
    if root == None:
        return 0
    elif root.left == None and root.right == None:
        return root.item
    else:
        return root.item + sum_total_nodes(root.left) + sum_total_nodes(root.right)

def check_identical(root1,root2):
    if root1 == None and root2 == None:
        return True
    elif root1 == None or root2 == None:
        return False
    else:
        if (root1 and root2)!= None:
            res = check_identical(root1.left,root2.left)
            if res == False:
                return False
            res2 = check_identical(root1.right,root2.right)
            if res2 == False:
                return False

    return True

def print_odd_nodes(root):

    if root!= None:
        if root.item %2 != 0:
            print(root.item)
        print_odd_nodes(root.left)
        print_odd_nodes(root.right)

def _find_largest_subtree(root):

    queue1 = Circular_Queue()
    queue1.append(root)
    empty = []
    while queue1.is_empty() == False:

        current = queue1.serve()
        if (current.left and current.right) != None:
            check = check_identical(current.left,current.right)
            if check == True:
                count = _level_order_traversal(current)
                empty.append((current.item,count))


        if current.left != None:
            queue1.append(current.left)
        if current.right != None:
            queue1.append(current.right)


    return empty

def check_tree_mirror(root1,root2):

    queue1 = Circular_Queue()
    queue2 = Circular_Queue()
    queue1.append(root1)
    queue2.append(root2)

    while (queue1.is_empty() == False and queue2.is_empty() == False):
        current1 = queue1.serve()
        current2 = queue2.serve()

        if (current1.left != None and current2.right!= None) and (current1.left.item == current2.right.item):
            queue1.append(current1.left)
            queue2.append(current2.right)

        if(current1.right != None and current2.left!= None) and ((current1.right.item == current2.left.item)):
            queue1.append(current1.right)
            queue2.append(current2.left)

        if (current1.left == None and current2.right!= None) or (current1.left != None and current2.right== None) or (current1.right == None and current2.left!= None) or (current1.right != None and current2.left== None):
            return False

        if ((current1.left!= None and current2.right!=None) and  (current1.left.item != current2.right.item)) or ((current1.right!= None and current2.left!=None) and (current1.right.item != current2.left.item)):
            return False

    return True

def sum_of_leaves(root):
    if root == None:
        return 0
    elif root.left == None and root.right == None:
        return root.item
    else:
        return sum_of_leaves(root.left) + sum_of_leaves(root.right)

def find_max_node(root):
    if root== None:
        return 0
    else:
        main = root.item
        max1 = find_max_node(root.left)
        max2 = find_max_node(root.right)
        if max1>max2:
            if max1 > main:
                return max1
            else:
                return main
        else:
            if max2 > main:
                return max2
            else:
                return main

def check_identical_subtrees(root):

    return _aux_check_identical_subtress(root.left,root.right)

def _aux_check_identical_subtress(root1,root2):
    if root1!= None and root2==None:
        return False
    elif root1 == None and root2!=None:
        return False
    elif root1 == None and root2 == None:
        return True
    else:
        check_left = _aux_check_identical_subtress(root1.left,root2.left)
        check_right = _aux_check_identical_subtress(root1.right,root2.right)
        if check_left == True and check_right == True:
            return True
        else:
            return False

def mirror(root):
    if root != None:
        mirror(root.left)
        mirror(root.right)
        root.left,root.right = root.right,root.left

def nodes_at_level(root,level):
    return _aux_nodes_at_level(root,0,level)

def _aux_nodes_at_level(root,count,level):
    if root == None:
        return 0
    elif root!= None and count== level:
        return 1
    else:
        sum_left = _aux_nodes_at_level(root.left,count+1,level)
        sum_right = _aux_nodes_at_level(root.right,count + 1, level)
        return sum_left + sum_right

def find_max_leaf(root):
    if root==None:
        return 0
    elif root.left == None and root.right==None:
        return root.item
    else:
        max_left_leaf = find_max_leaf(root.left)
        max_right_leaf = find_max_leaf(root.right)
        if max_left_leaf>= max_right_leaf:
            return max_left_leaf
        else:
            return max_right_leaf

def check_sum_tree(root):
    check = _aux_check_sum_tree(root)
    if check!= False:
        return True
    return False

def _aux_check_sum_tree(root):
    if root == None:
        return 0
    elif (root.left==None and root.right == None):
        return root.item
    else:
        save_root = root.item
        sum_left = _aux_check_sum_tree(root.left)
        sum_right = _aux_check_sum_tree(root.right)
        if  (sum_left!= False and sum_right!= False ) and (sum_left + sum_right == save_root):
            return save_root + sum_left + sum_right
        else:
            return False

def find_right_and_left_mostleaf(root):
    result = _aux_left_right_(root,[])
    if len(result) == 1:
        print('Both left-most leaf and right-most leaf is same: ' + str(result[0]))
    else:
        print('Left-most leaf is ' + str(result[0]))
        print('Right-most leaf is ' + str(result[len(result)-1]))

def _aux_left_right_(root,leaves):
    if root==None:
        return
    elif (root.left == None and root.right == None):
        leaves.append(root.item)
        return
    else:
        _aux_left_right_(root.left,leaves)
        _aux_left_right_(root.right,leaves)
        return leaves

def _print_nodes_at_level(root,count,level):
    if root == None:
        return 0
    elif root!= None and count== level:
        print(root.item,end=' ')
        return 1
    else:
        sum_left = _print_nodes_at_level(root.left,count+1,level)
        sum_right = _print_nodes_at_level(root.right,count + 1, level)
        return sum_left + sum_right

def level_order_traversal_recursive(root):


    result = 1
    level = 0
    while result != 0:
        result = _print_nodes_at_level(tree1.root,0,level)
        print()
        level += 1

def left_view(root):
    _aux_left_view(root,0)

def _aux_left_view(root,side):
    if root!= None:
        if side == 0:
            print(root.item,end=' ')
        _aux_left_view(root.left,0)
        _aux_left_view(root.right,1)

def inorder_without_recursion(root):
    stack = Stack()
    current = root
    stack.push(current)

    while stack.is_empty()!= True:
        if current!=None:
            current = current.left
        elif current == None:
            current = stack.pop()
            print(current.item)
            current = current.right
        if current!= None:
            stack.push(current)

def max_path_sum(root):
    if root==None:
        return 0
    else:
        sum = root.item
        sum1 = root.item + max_path_sum(root.left)
        sum2 = root.item + max_path_sum(root.right)
        sum3 = root.item + max_path_sum(root.left) + max_path_sum(root.right)
    return max(sum,sum1,sum2,sum3)

def level_ordertraversal(root):

    queue = Circular_Queue()

    queue.append(root)
    check = True
    while queue.is_empty() != True:
        node = queue.serve()

        if check == False and (node.left != None and node.right != None):
            return False

        elif (node.left== None) and (node.right!= None):
            return False
        elif (node.left == None or node.right == None):
            check = False

        if node.left != None:
            queue.append(node.left)
        if node.right!= None:
            queue.append(node.right)

    return True

def eval_expressiontree(root):

    if root.left == None and root.right == None:
        return root.item

    else:
        left_leaf = eval_expressiontree(root.left)
        operator = root.item
        right_leaf = eval_expressiontree(root.right)
        return eval(left_leaf,right_leaf,operator)


def eval(left,right,op):
    if op == '+':
        return left+right
    elif op == '-':
        return left-right
    elif op == '*':
        return left*right
    else:
        return left/right

def collect_leaves(root,the_list):
    if root == None:
        return []
    elif (root.left == None) and (root.right == None):
        return [root.item]
    else:
        return collect_leaves(root.left,[]) + collect_leaves(root.right,[])


def longest_consecutive_sequence_node(root,parent,count):

    if root == None:
        return count-1
    elif (parent.item + 1 != root.item) and root!= parent:
        return count-1
    else:

        max_left = longest_consecutive_sequence_node(root.left,root,count+1)
        max_right = longest_consecutive_sequence_node(root.right,root,count+1)
        if max_left > max_right:
            return max_left
        else:
            return max_right

def _level_order_traversal_iterative_modified(root):

    queue = Circular_Queue()
    queue.append(root)
    max = 0

    while queue.is_empty() == False:

        current = queue.serve()
        new_max = longest_consecutive_sequence(current, current, 1)

        if new_max > max:
            max = new_max
        if current.left != None:
            queue.append(current.left)
        if current.right != None:
            queue.append(current.right)

    return max

def longest_consecutive_sequence_recur(root,parent,temp,Max):

        if root == None:
            return Max
        if (parent.item + 1 == root.item):
            temp+=1
        if temp > Max:
            Max = temp
        if (parent.item + 1 != root.item):
            temp = 1

        max_left = longest_consecutive_sequence_recur(root.left,root,temp,Max)
        max_right = longest_consecutive_sequence_recur(root.right, root, temp, Max)
        return max(max_left,max_right)

def get_min_top_complete_bst(root,parent):
    if root == None:
        return None
    elif (root.left == None and root.right == None):
        return root.item
    else:
        min_left = get_min_top_complete_bst(root.left,root)
        min_right = get_min_top_complete_bst(root.right,root)
        if (min_right == None and min_left < root.item):
            root.left.item,root.item = root.item,root.left.item
        elif root.item > min_left and min_left < min_right:
            root.left.item, root.item = root.item, root.left.item
        elif (min_right != None and root.item > min_right and min_right < min_left):
            root.right.item, root.item = root.item, root.right.item
        return root.item

def convert_complete_binary_to_min_heap(copy):

    if copy == None:
        return
    else:
        get_min_top_complete_bst(copy,copy)
        convert_complete_binary_to_min_heap(copy.left)
        convert_complete_binary_to_min_heap(copy.right)








#Print extreme nodes of each level of Binary Tree in alternate order
#Inorder Tree Traversal without Recursion
#Maximum Path Sum in a Binary Tree
#Maximum Consecutive Increasing Path Length in Binary Tree


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






if __name__ == '__main__':
    tree1 = BinaryTree()
    tree1.add(3,'')
    tree1.add(2,'0')
    tree1.add(10,'1')
    tree1.add(1,'00')
    tree1.add(-1,'01')
    tree1.add(-2,'10')
    #level_order_traversal(tree1.root)

    convert_complete_binary_to_min_heap(tree1.root)

    level_order_traversal(tree1.root)














