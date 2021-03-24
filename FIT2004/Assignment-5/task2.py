from stack_ADT import Stack

def find_all_subsets(m,filename):
    """
                                                    This function finds path from one vertice to the same vertice
                                                    :param m: number of subsets
                                                    :param filename: file to write
                                                    :return: None
                                                    :raises: None
                                                    :precondition: valid parameters
                                                    :complexity: best and worst case is O(2**m)
                                                    :postcondition: SUBSETS written to file
                                                    """

    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m']
    file = open(filename,'w')
    for i in range(2**m):
        file.write('subset ' + str(i+1) + ':   ' + '\t\t' + '{' + make_subset(letters,convert_binary_to_gray_code(find_binary(i,m))) + '}' +'\n')
def make_subset(set,binary):
    """
                                                    This function makes subset from binary
                                                    :param set: all letters
                                                    :param binary: binary number
                                                    :return: string
                                                    :raises: None
                                                    :precondition: valid parameters
                                                    :complexity:  best and worst case is O(E) where E is the length of binary
                                                    :postcondition: string formed
                                                    """
    string = ''
    for index, item in enumerate(binary):
        if item == '1':
            string+=set[index]
    return string
def convert_binary_to_gray_code(binary):
    """
                                                    This function finds the gray code of binary
                                                    :param binary: binary
                                                    :return: string
                                                    :raises: None
                                                    :precondition: valid parameters
                                                    :complexity:  best and worst case is O(E) where E is the length of binary
                                                    :postcondition: string found
                                                    """
    string = '' + binary[0]
    for i in range(0,len(binary)-1):
        string+= (XOR(binary[i],binary[i+1]))

    return string
def XOR(x,y):
    """
                                                    This function finds xor of two numbers
                                                    :param x: first number
                                                    :param y: second number
                                                    :precondition: valid parameters
                                                    :complexity:  best and worst case is O(1)
                                                    :postcondition: xor returned
                                                    """

    if (x == '1' and y == '1') or ( x == '0' and y == '0'):
        return '0'
    else:
        return '1'
def find_binary(decimal_number,size):
    """
                                                    This function converts decimal to binary
                                                    :param decNumber: decimal number
                                                    :param size: size 
                                                    :return: binary
                                                    :raises: None
                                                    :precondition: valid parameters
                                                    :complexity:  best and worst case is O(logn) where n is the number
                                                    :postcondition: binary found
                                                    """

    myStack = Stack()

    while decimal_number > 0:
        rem = decimal_number % 2
        myStack.push(rem)
        decimal_number = decimal_number // 2

    binary_string = ""
    while not myStack.is_empty():
        binary_string = binary_string + str(myStack.pop())

    if len(binary_string)<size:
        while len(binary_string)!= size:
            binary_string = '0' + binary_string
    return binary_string

if __name__ == '__main__':
    n = int(input('n: '))
    assert (n >= 2 and n <= 10), "Please keep n between 2 and 3"
    find_all_subsets(n,'outputTask2.txt')