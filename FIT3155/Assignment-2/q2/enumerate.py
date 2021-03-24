import math
import argparse
#NAME - HUSSAIN SADIQ ABUWALA
#STUDENT-ID - 27502333
'''
Description: finds the next start position
Algorithm used: using the "011" technique with recursion
Param:  prev_tree
Param:  index
Param:  curr_trees_arr
return: index
'''
def find_next_start(prev_tree,index,curr_trees_arr):

    if(prev_tree[index] == "1"):

        # Detected a leaf
        # recurse back
        if(index + 1 < len(prev_tree)):
            new_tree = prev_tree[:index] + "011" + prev_tree[index + 1:]
        else:
            new_tree = prev_tree[:index] + "011"

        addArr(curr_trees_arr,new_tree)
        return index + 1

    else:

        # preorder traversal - Root, left, right
        # implicitly i am currently at the root ar 'index' or root = bit_string[index]

        # go left
        l = find_next_start(prev_tree,index + 1,curr_trees_arr)
        r = find_next_start(prev_tree,l,curr_trees_arr)
        return r


'''
Description: converts binary to decimal value
Param:  binary number
return: decimal value
'''
def bin_to_dec(binary_num):
    return int(binary_num,2)

'''
Description: add tree to array if does not exist already    
Param: arr
Param: string 
return: None
'''
def addArr(arr,string):

    if(arr == []):
        arr.append(string)
    else:
        dec = bin_to_dec(string)
        prev_dec = bin_to_dec(arr[len(arr) - 1])
        if(dec <= prev_dec):
            return
        else:
            arr.append(string)


'''
Description: enumerate all trees till N
Param:  N
Param: all trees
return: all trees till N
'''
def enumarate_b_trees_till_N(N,all_trees):

    if(N == 0):
        all_trees[N] = ["1"]
        return ["1"]
    else:

        my_tree = []
        prev_trees = enumarate_b_trees_till_N(N - 1,all_trees)
        for tree in prev_trees:
            find_next_start(tree,0,my_tree)

        all_trees[N] = my_tree
        return my_tree

def main(N):

    all_trees = [None] * (N + 1)
    enumarate_b_trees_till_N(N,all_trees)
    return all_trees

def run_command_line():

    parser = argparse.ArgumentParser()
    parser.add_argument('N',type=int)
    args = parser.parse_args()

    N = args.N
    all_trees = main(N)

    file = open('output_enumerate.txt', 'w')

    count = 1
    for item in all_trees:
        for tree_code in item:
            file.write(str(count) + "    " + tree_code + "\n")
            count += 1

    file.close()

if __name__ == '__main__':

    #main(4)
    #find_next_start("0001111",0,arr)
    #print(arr)
    #print(calculate_total_b_tree(10))
    run_command_line()