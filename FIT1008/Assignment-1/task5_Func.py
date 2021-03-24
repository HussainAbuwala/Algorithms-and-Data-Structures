
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

    user_temp = int(input('Enter the temperature you want to find'))
    linear_Search(user_temp,the_list,size)

def linear_Search(temp,lists,length):

    '''
    This functions implements linear search
    :param temp: the temperature to find
    :param lists: the list of values
    :param length: the length of the list
    :return: nothing
    :raise: no exceptions
    :precondition: none
    :complexity:best case 0(1), worst case 0(n), where n is the len(lists)
    
    '''
    check = 'F'
    check1 = 'T'
    j = 0
    while (j < length):
        if lists[j] == temp:
            check = check1
            break
        j = j + 1

    if (check != check1):
        print('Temperature not found')
    else:
        print('Temperature found')


main()
