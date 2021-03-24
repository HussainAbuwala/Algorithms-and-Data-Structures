import sys

def main():

    
    '''
    This function implements the creating and inserting values into the list
    and calling other functions
    :param : none
    :return: does not return anything
    :raise: no exceptions
    :precondition: none
    :complexity: 0(n) for the while loop and summation of the respective time
    complextys of the other functions which are called
    
    '''
    size = int(input('Enter the size of the list'))

    the_list = [0]*size
    m = 0
    while m < (size):
        the_list[m] = int(input('Value: '))
        m = m + 1

    SortByTemp(the_list,size)
    print(the_list)
    temp = int(input('enter temperature to find'))
    x = binarySearch(the_list,0,size-1,temp)
    print('Your item is found at index ' + str(x))



    


def SortByTemp(lists,length):

    '''
    This function implements the insertion sort
    :param lists: list which needs to be sorted
    :param length: length of the list
    :return: does not return anything
    :raise: no exceptions
    :precondition: none
    :complexity: best case 0(n), worst case 0(n^2)
    
    '''
    i = 1
    j = 0
    while i<length:
        val = lists[i]
        j = i - 1
        while (j >= 0) and (lists[j] > val):
            swap(lists,j)
            j = j - 1
            
        lists[j+1] = val
        i = i+1

def swap(lists1,position):

    '''
    This function implements the swapping of values in the list
    :param lists1: list which needs to be sorted
    :param position: index which can be used to swap the values
    :return: does not return anything
    :raise: no exceptions
    :precondition: none
    :complexity: best case 0(1), worst case 0(1)
    
    '''
    temp1 = lists1[position]
    lists1[position+1] = temp1

def binarySearch (arr, l, r, x):

    '''
    This functions implements binary search
    :param arr: a sorted list
    :param l:starting index of list
    :param r:last index of list
    :param x:temperature to find
    :return: the index of item if item in the list else prints item not found
    :raise: no exceptions
    :precondition: arr must be sorted in increasing order
    :complexity:best case 0(1), worst case 0(log n), where n is the len(arr)
    
    '''
 
    # Check base case
    if r >= l:
 
        mid = l + ((r - l)//2) 
        # If element is present at the middle itself
        if arr[mid] == x:
            result = mid
         
        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            result =  binarySearch(arr, l, mid-1, x)
 
        # Else the element can only be present in right subarray
        else:
            result =  binarySearch(arr, mid+1, r, x)
            
        return result
 
    else:
        # Element is not present in the array
        print('Temperature not found')
        sys.exit()

main()
