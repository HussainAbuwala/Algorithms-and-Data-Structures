import math
from print_all_possible_paths import find_all_trees
from print_all_possible_paths import find_target_path_pos
import argparse


'''
Description: this is a preorder traversal of the tree code
Algorithm used: pre_order traversal
Param:  bit string
Param:  index
return: index
'''

def find_next_start(bit_string,index):

    if(bit_string[index] == "1"):

        # Detected a leaf
        # recurse back
        return index + 1
    else:

        # preorder traversal - Root, left, right
        # implicitly i am currently at the root ar 'index' or root = bit_string[index]

        # go left
        l = find_next_start(bit_string,index + 1)
        r = find_next_start(bit_string,l)
        return r

'''
Description: convert binary to decimal
Param: binary number
return: decimal
'''
def bin_to_dec(binary_num):
    return int(binary_num,2)


def find_decode_strings(bit_string):

    strings_to_decode = []
    index = 0

    while (index < len(bit_string)):
        new_start = find_next_start(bit_string,index)
        strings_to_decode.append(bit_string[index:new_start])
        index = new_start

    return strings_to_decode


'''
Description: finds the total number of trees with N internal nodes
Algorithm used: formula of catalan
Param:  N
return: total trees with N internal nodes
'''
def find_total_no_of_bt(N):

    numerator = math.factorial(2 * N)
    denominator = math.factorial(N + 1) * math.factorial(N)
    return numerator // denominator


'''
Description: finds the different tree codes
Algorithm used: each tree code is found when number of leaf nodes is > than number of internal nodes
Param:  bit_string
return: all tree codes to be decoded
'''
def break_up_trees(bit_string):

    no_of_leaves = 0
    no_of_internal_nodes = 0
    start_index = 0
    trees_to_decode = []
    for i in range(len(bit_string)):

        if (no_of_leaves == no_of_internal_nodes + 1):
            trees_to_decode.append([bit_string[start_index:i],no_of_internal_nodes,bin_to_dec(bit_string[start_index:i])])
            no_of_leaves = 0
            no_of_internal_nodes = 0
            start_index = i

        if(bit_string[i] == "0"):
            no_of_internal_nodes += 1

        if(bit_string[i] == "1"):
            no_of_leaves += 1

    trees_to_decode.append([bit_string[start_index:len(bit_string)],no_of_internal_nodes,bin_to_dec(bit_string[start_index:len(bit_string)])])


    return trees_to_decode

'''
def main_v2(bit_string):
    trees_to_decode = break_up_trees(bit_string)

    max_internal_node = trees_to_decode[0][1]

    for tree_code in trees_to_decode:

        if (tree_code[1] > max_internal_node):
            max_internal_node = tree_code[1]

    dp_arr_total_trees = [None] * (max_internal_node + 1)
    dp_arr_total_trees[0] = 1
    for i in range(1,len(dp_arr_total_trees)):
        dp_arr_total_trees[i] = find_total_no_of_bt(i) + dp_arr_total_trees[i-1]

    decoded_integers = []
    for tree_code_tuple in trees_to_decode:
        tree_code = tree_code_tuple[0]
        internal_node = tree_code_tuple[1]

        if (internal_node == 0):
            decoded_integers.append(1)

        elif (internal_node == 1):
            decoded_integers.append(2)

        else:
            offset = find_target_path_pos(internal_node,tree_code)
            decoded_integers.append(dp_arr_total_trees[internal_node - 1] + offset)
            print(decoded_integers)


    return decoded_integers'''


'''
Description: decodes all tree codes to integer
Algorithm used: for each tree_code, all paths in the matrix are found for some N. Then binary search is used
Param:  bit_string
return: decoded integers
'''

def main(bit_string):

    trees_to_decode = break_up_trees(bit_string)

    max_internal_node = trees_to_decode[0][1]

    for tree_code in trees_to_decode:

        if(tree_code[1] > max_internal_node):
            max_internal_node = tree_code[1]


    dp_arr_trees = [None] * (max_internal_node + 1)
    dp_arr_total_trees = [None] * (max_internal_node + 1)

    dp_arr_total_trees[0] = 1
    for i in range(1,len(dp_arr_total_trees)):
        dp_arr_total_trees[i] = find_total_no_of_bt(i) + dp_arr_total_trees[i-1]

    decoded_integers = []
    for tree_code in trees_to_decode:
        internal_node = tree_code[1]
        tree_code_dec = tree_code[2]

        if(internal_node == 0):
            decoded_integers.append(1)

        elif(internal_node == 1):
            decoded_integers.append(2)

        elif(dp_arr_trees[internal_node] == None):
            all_trees = find_all_trees(internal_node)
            dp_arr_trees[internal_node] = all_trees
            result = binarySearch(all_trees, tree_code_dec)
            if(result!= False):
                pos = result[1]
                offset = pos + 1
                decoded_integers.append(dp_arr_total_trees[internal_node - 1] + offset)

        else:
            all_trees = dp_arr_trees[internal_node]
            result = binarySearch(all_trees,tree_code_dec)
            if(result != False):
                pos = result[1]
                offset = pos + 1
                decoded_integers.append(dp_arr_total_trees[internal_node-1] + offset)

    return decoded_integers


'''
Description: binary search
Param:  list to search for
Param:  item to find
return: index of the found item
'''



def binarySearch(alist, item):
    first = 0
    last = len(alist)-1
    found = False

    while first<=last and not found:
        midpoint = (first + last)//2
        if alist[midpoint] == item:
            found = (True,midpoint)
            return found
        else:
            if item < alist[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1


    return found


def run_command_line():

    parser = argparse.ArgumentParser()
    parser.add_argument('textFile',type=argparse.FileType('r'))
    args = parser.parse_args()

    text = ""

    for line in args.textFile.read():
        text+= line.strip()

    final_result = main(text)

    file = open('output_intseqdecode.txt', 'w')

    for item in final_result:
        file.write(str(item))
        file.write(",")

    file.close()



if __name__ == '__main__':
    run_command_line()