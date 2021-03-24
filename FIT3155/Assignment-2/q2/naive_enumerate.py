import argparse
#NAME - HUSSAIN SADIQ ABUWALA
#STUDENT-ID - 27502333
'''
Description: finds all trees using finding all trees on the left and right and joining with root
Param:  N
Param:  dp_array - if tree already found, no need to compute again
return: index
'''

def enum(N,dp_array):

    if(dp_array[N] != None):
        return dp_array[N]
    elif(N == 0):
        dp_array[0] = ["1"]
        return ["1"]
    else:
        n_minus_one = N - 1
        my_trees = []
        left = n_minus_one
        right = 0

        while (left >=0):

            left_trees = enum(left,dp_array)
            right_trees = enum(right,dp_array)
            aux_tree = addRoot(findComb(left_trees,right_trees))
            my_trees = my_trees + aux_tree
            left -= 1
            right += 1

        dp_array[N] = my_trees
        return my_trees


'''
Description: add root to all trees
Param:  trees
return: rooted trees
'''
def addRoot(trees):
    for i in range(len(trees)):
        trees[i] = "0" + trees[i]
    return trees

'''
Description: find all combinations between two lists
Param:  list 1
Param:  list 2
return: all combinations
'''
def findComb(l1,l2):
    return [str(x) + str(y) for x in l1 for y in l2]

'''
Description: convert binary to decimal
Param:  binary number
return: decimal number
'''
def bin_to_dec(binary_num):
    return int(binary_num,2)


'''
Description: convert to decimal
Param:  arr
return: decimals list
'''
def convert_to_decimal(arr):
    x = []
    for item in arr:
        x.append((item,bin_to_dec(item)))
    return x


'''
Description: sorts the list
Algorithm used: merge sort
Param:  list
return: none
'''
def mergeSort(alist):
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if compare(lefthalf[i],righthalf[j]):
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1

def compare(a,b):

    if(a[1] < b[1]):
        return True
    else:
        return False


def main(N):
    dp_array = [None] * (N + 1)
    enum(N, dp_array)

    decimals = []
    for item in dp_array:
        decimals.append(convert_to_decimal(item))

    for item in decimals:
        mergeSort(item)

    return decimals



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
            file.write(str(count) + "    " + tree_code[0] + "\n")
            count += 1

    file.close()

if __name__ == '__main__':

    #main(10)
    run_command_line()