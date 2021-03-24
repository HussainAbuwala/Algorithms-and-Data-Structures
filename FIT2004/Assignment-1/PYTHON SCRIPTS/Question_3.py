from random_functions import *
from Question_1 import conv_dec_fact_base
def fact_base_to_permute_string(factbase,N):
    """
            This function converts factorial base to permutation string
            :param factbase: inumber
            :param N: length of permuatation
            :return: permutation string
            :raises: None
            :precondition: string and integer number N
            :complexity: best and worst case is O(n^2) where n is the size of the array.
            :postcondition: permuation string is returned
            """

    alphabets = ""

    for i in range(N):
        alphabets+= str(i+1)

    permuteString = ""
    for i in range(len(factbase)):
        permuteString+= alphabets[int(factbase[i])]
        alphabets = new_string(alphabets,factbase[i])

    return permuteString

def cal_determinant_matrices(matrix):
    """
            This function returns determinant
            :param matrix: nested table
            :return: determinant
            :raises: None
            :precondition: square matrix
            :complexity: best and worst case is O(n^2n!) where n is the size of the array.
            :postcondition: determinant is returned
            """

    if not check_square(matrix):                        #n times
        return False                                    #1 times

    n = len(matrix)
    fact = factorial_of_number(n)                       #n times
    permlist = []                                       #constant operation done 1 times
    factbase = []                                       ##constant operation done 1 times

    for i in range(fact):                               #In best and worst case, runs n! times
        x = conv_dec_fact_base(i,n)                     #In best and worst case, runs n^2 times for each iteration of the outer loop
        y = fact_base_to_permute_string(x,n)            #In best and worst case, runs n^2 times for each iteration of the outer loop
        permlist.append(y)                              #runs n! times
        factbase.append(x)                              #runs n! times

    r = 1                                               #constant operation done 1 times
    sum = 0                                             #constant operation done 1 times

    for i in range(len(permlist)):                      #In best and worst case, runs n! times
        y = permlist[i]                                 #constant operation, done n! times
        for j in range(n):                              #runs n times in best and worst case for every iteration of the outer loop
            r = r * int(matrix[int(y[j]) - 1][j])       #constant operation done n times for every iteration of the outer loop

        r = r * sign(factbase[i])                       #calculated n times for every iteration of the outer loop
        sum += r                                        #constant operation, done n! times
        r = 1                                           #constant operation, done n! times

    return sum

#Final equations = n + 1 + n + 1 + 1 + n! + (n^2 * n!) + (n^2 * n!) + n! + n! + 1 + 1 + n! + n! + (n * n!) + (n * n!) + (n * n!) + n! + n! + 1
#                = 2n + 6 + 7n! + 2n^2n! + 3nn!
#                = 2n^2n! + 3nn! + 7n! + 2n + 6
#Big-Oh Notation = O(n^2n!)


def sign(perm):
    """
            This function finds the sign
            :param perm: factorial base
            :param N: length of permuatation
            :return: +1 if even and -1 if odd
            :raises: None
            :precondition: factorial base
            :complexity: best and worst case is O(n) where n is the length of the factorial base.
            :postcondition: sign returned
            """

    sum = 0
    for i in range(len(perm)):
        sum+= int(perm[i])

    if (sum % 2 == 0):
        return 1
    return -1

def check_square(matrix):
    """
                This function checks if matrix is square
                :param matrix: nested
                :return: True or False depending on matrix
                :raises: None
                :precondition: nested
                :complexity: best and worst case is O(n) where n is the length of the matrix.
                :postcondition: verified if square
                """

    row_length = len(matrix)
    for item in matrix:
        if len(item)!= row_length:
            return False
    return True

if __name__ == '__main__':
    infile = open('matrix2','r')                                                        #opens the file in reading mode
    contents = infile.readlines()                                                       #reads the files as a list of lines and stores it in the contents variable
    infile.close()

    for i in range (len(contents)):
        contents[i] = (contents[i].rstrip('\n')).split(',')


    determinant = cal_determinant_matrices(contents)
    if determinant == False:
        print('ERROR')
    else:
        print ("N = " + str(len(contents)))
        print ('Input Matrix: ')

        for i in range(len(contents)):
            for j in range(len(contents)):
                print(contents[i][j],end = '\t\t')
            print()

        print("Determinant = " + str(determinant))




