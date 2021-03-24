from hash_table_task8 import QuadraticProbeTable
import decimal

def optimalCost_BST_bottom_up(keys,probability,frequencies):
    """
        This function finds the minimum cost bst
        :param keys: words
        :param probability: empirical probabilities of each word (list)
        :param hashtablefreq: hashtable of frequencies of each word
        :return: None
        :raises: None
        :precondition: valid parametes
        :complexity: best and worst case is O(n^2) where n is the number of keys.
        :postcondition: optimal bst found
        """

    new_array_rows = len(keys)
    costMatrix = []
    rootMatrix = []
    weightMatrix = []

    for i in range(new_array_rows):
        costMatrix.append([0] * new_array_rows)     #making the matrix
        rootMatrix.append([0] * new_array_rows)
        weightMatrix.append([0] * new_array_rows)

    for i in range(len(costMatrix)):                #initialising values
        costMatrix[i][i] = probability[i]
        rootMatrix[i][i] = i
        weightMatrix[i][i] = probability[i]

    for i in range (1,len(costMatrix)):             #incresing the range of roots
        for j in range(0,(len(costMatrix))-i):      #move verticall to find different combinations of optimal roots
            cost_left, cost_right, min, k = 0,0,float('inf'),0
            weightMatrix[j][i + j] = weightMatrix[j][i+j-1] + weightMatrix[i + j][i + j]
            for root in range(rootMatrix[j][i+j-1],rootMatrix[j+1][i+j] + 1):#j,i+j+1   #optimisation
                if (root-1) >= 0: cost_left = costMatrix[j][root - 1]
                if (root+1) < len(costMatrix): cost_right = costMatrix[root + 1][i + j]
                value = cost_left + cost_right + weightMatrix[j][i + j]
                if value < min:
                    min = value
                    k = root
                cost_left, cost_right = 0,0
            costMatrix[j][i + j] = min
            rootMatrix[j][i + j] = k

    hashtable = QuadraticProbeTable()
    find_level_keys(0,len(rootMatrix)-1,1,hashtable,rootMatrix,keys)
    find_cumilative_sum(keys,probability,hashtable,frequencies)

def find_level_keys(i,j,level,hashtable,rootMatrix,keys):
    """
            This function calcuates level of each word
            :param i: starting index
            :param j: ending index
            :param level: level of each key
            :param hashtable: to store key and level
            :param keys: list of keys
            :return: None
            :raises: None
            :precondition: valid parameters
            :complexity: best and worst case is O(2^n) where n is the number of keys.
            :postcondition: level of each key is found
            """

    if (j < i ) or (i > j):
        return
    else:
        hashtable[keys[rootMatrix[i][j]]] = level
        find_level_keys(i,rootMatrix[i][j]-1,level+1,hashtable,rootMatrix,keys)
        find_level_keys(rootMatrix[i][j]+1,j,level+1,hashtable,rootMatrix,keys)

def find_probability_keys(filename):
    """
            This function finds the empirical probability of each key
            :param filename: name of file
            :return: None
            :raises: None
            :precondition: valid parametes
            :complexity: best and worst case is O(1), actually "amortized" O(1).
            :postcondition: optimal bst found
            """
    file, words, probabilities, frequency = open(filename, 'r'), [], [], []
    count = 0


    for item in file:
        item = item.strip('\n').split(' ')
        count += int(item[1])
        words.append(item[0])
        frequency.append(int(item[1]))

    for i in range(len(words)):
        probabilities.append(frequency[i] / count)

    optimalCost_BST_bottom_up(words, probabilities, frequency)

def find_cumilative_sum(keys,probabilities,hashtablelevel,frequencies):
    """
            This function finds the cumilative frequency of each key
            :param keys: words
            :param probability: empirical probabilities of each key (list)
            :param hashtablelevel: hashtable of levels of each key
            :param hashtablefreq: hashtable of frequencies of each key
            :return: None
            :raises: None
            :precondition: valid parameters
            :complexity: best and worst case is O(n) where n is the number of keys.
            :postcondition: optimal bst found
            """

    file = open('microbst.txt','w')
    cumilative_frequencies = []
    cumilative_frequencies.append(probabilities[0] * hashtablelevel[keys[0]])

    for i in range(1,len(keys)):
        cumilative_frequencies.append(cumilative_frequencies[i-1] + (probabilities[i] * hashtablelevel[keys[i]]))

    file.write('{0:>20} {1:>30} {2:>20} {3:>30}'.format('Key (K_i)', 'Freq of Key K_i', 'Level of K_i','Cumilative Sum') + '\n')
    file.write('\n')
    for i in range(len(keys)):
        file.write('{0:>20} {1:>30} {2:>20} {3:>30}'.format(keys[i],frequencies[i],hashtablelevel[keys[i]],cumilative_frequencies[i]) + '\n')

find_probability_keys('FREQUENCY.txt')

