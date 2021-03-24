def cal_aver(lists,length):

    '''
    This functions implements calculating average of the values in list
    :param lists: the list of values
    :param length: the length of the list
    :return: the average value stored in the final variable
    :raise: no exceptions
    :precondition: none
    :complexity:best case 0(n), worst case 0(n), where n is the len(lists)
    
    '''
    total = 0
    value = 0
    final = 0
    j = 0
    while j< (length):
        value = lists[j]
        total = total + value
        j = j+1

    final = total //length

    return final

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
    i = 0
    while i < (size):
        the_list[i] = int(input('Value: '))
        i = i+1

    average = cal_aver(the_list,size)
    print(average)


main()
    
