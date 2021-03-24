from random_functions import *

def min_swaps(string,string1):
    """
       This function calcualates min swaps
       :param string: string
       :param string1: string
       :return: min swaps
       :raises: None
       :precondition: two strings which have the same letters and length
       :complexity: best and worst case is O(n^2) where n is the length of permuation.
       """
    sum = 0

    for i in range(len(string1)):
        val = find_index(string1[i],string)
        sum = val + sum
        string = new_string(string,val)

    return sum

if __name__ == '__main__':
    x = input("")
    y = input("")
    print("Input Permutation 1: " + x )
    print("Input Permutation 2: " + y )
    print("Ouput (smallest number of inversions) = " + str(min_swaps(x,y)) )


