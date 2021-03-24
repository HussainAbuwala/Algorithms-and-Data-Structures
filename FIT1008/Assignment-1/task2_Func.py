upper = 0
lower = 0

size = int(input('Enter the size of the list'))

the_list = [0]*size
i = 0

while i < (size):
    the_list[i] = int(input('Value: '))
    i = i + 1
    
lower = 0
upper= size -1


def list_reverse(the_list,upper_list,lower_list):

    '''
    This functions implements printing values in list in reverse order
    :param upper_list: index of the last value of the list
    :param lists: the list of values
    :param lower_list: index of first value in the list
    :return: nothing
    :raise: no exceptions
    :precondition: none
    :complexity:best case 0(1), worst case 0(n), where n is the len(lists)
    
    '''
    
    while (upper_list >= lower_list):

        a = the_list[upper_list]
        print(a,end=' ')
        upper_list = upper_list - 1
        
      
list_reverse(the_list,upper,lower)
