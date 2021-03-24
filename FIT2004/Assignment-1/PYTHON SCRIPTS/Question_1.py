from random_functions import *
from hash_tables_linear_probing import LinearProbeTable

def conv_dec_fact_base(dec_number, N):
    """
    This function converts decimal to base factorial
    :param dec_number: inumber
    :param N: length of permuatation
    :return: factorial base
    :raises: None
    :precondition: integer numbers
    :complexity: best and worst case is O(n^2) where n is the size of the array.
    :postcondition: factorial base is returned
    """
    factbase = ""
    for i in range (N-1,-1,-1):
        x = factorial_of_number(i)
        factbase += str(dec_number//x)
        dec_number = dec_number % x
    return factbase


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

    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    alphabets = ""

    for i in range(N):
        alphabets+= letters[i]

    permuteString = ""
    for i in range(len(factbase)):
        permuteString+= alphabets[int(factbase[i])]
        alphabets = new_string(alphabets,factbase[i])
    return permuteString

def test_function(N):
    hashtable = LinearProbeTable()
    fact = factorial_of_number(N)
    container = []
    container.append('Input to the script: N = ' + str(N))
    container.append('Total Number of Permuatations: ' + str(fact))
    container.append('{0:>20} {1:>30} {2:>30} {3:>30}'.format("Base-10", "Base-!", "Sum", "Permutations"))
    container.append("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")


    for i in range(fact):
        x = conv_dec_fact_base(i, N)
        y = str(sum_of_factbase(x))
        container.append('{0:>20} {1:>30} {2:>30} {3:>30}'.format("(" + str(i) + ")" + "_10", "(" + x + ")" + "_!",y,fact_base_to_permute_string(x, N)))
        hashtable[y] = 1

    container.append("\n")
    container.append('{0:>20} {1:>30}'.format("Sum","Frequency"))
    container.append("---------------------------------------------------------------------------------------------")

    frequeuncy = 0
    weight = 0
    for i in range (int(y)+1):
        try:
            y = hashtable[str(i)]
            frequeuncy += y
            weight = weight + (i * y)
            container.append('{0:>20} {1:>30}'.format(str(i),str(y)))
        except KeyError:
            continue

    container.append("\n")
    container.append('Weighted Average =  ' + str(weight/frequeuncy))

    write_to_file("PERMUTATIONS.txt", container)


if __name__ == '__main__':
    x = int(input(""))
    if x == 0:
        print('ERROR')
    else:
        test_function(x)




