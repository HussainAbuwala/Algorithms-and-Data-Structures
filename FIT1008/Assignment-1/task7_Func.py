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
    median(the_list,size)

    


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
    

def median(lst,Size):

    '''
    This function implements calculation of median value of list
    :param lst: sorted list
    :param size: length of the list
    :return: does not return anything
    :raise: no exceptions
    :precondition: list needs to be sorted
    :complexity: best case 0(1), worst case 0(1)
    
    '''   
    index = (Size - 1) // 2
    if (Size % 2 !=0):
        print( lst[index])
    else:
        first_index = lst[index]
        sec_index = lst[index + 1]
        result = int((first_index + sec_index)//2.0)
        print(result)


main()
