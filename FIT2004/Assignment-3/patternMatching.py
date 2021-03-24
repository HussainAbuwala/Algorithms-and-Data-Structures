from heap import heap_sort
from lf_mapping_to_suffix_array import lf_mapping_to_suffix_array

def read_file(filename):
    """
                This function reads lines from a file
                :param filename: name of the file to be read
                :return: bwt string
                :raises: None
                :precondition: valid filename
                :complexity: best and worst case is O(1).
                :postcondition: string returned
                """

    file = open(filename, "r")
    string = file.readline().strip('\n')

    return string

def compute_occurences(bwt_string):
    """
                This function find the occurences
                :return: bwt string
                :raises: None
                :precondition: valid bwt
                :complexity: best and worst case is O(n) where n is length of bwt_string.
                :postcondition: occurences returned
                """
    array = [None] * 256
    i = 0
    count = 0

    for j in range(len(bwt_string)):
        if array[ord(bwt_string[j])] == None:
            array[ord(bwt_string[j])] = i
            i+=1
            count+=1

    occurences = [0] * count

    for i in range(len(occurences)):
        occurences[i] = [0] * len(bwt_string)


    for i in range(count):
        for j in range(len(bwt_string)):
            if (array[ord(bwt_string[j])]) == i:
                if (j - 1) < 0:
                    occurences[i][j] = 1
                else:
                    occurences[i][j] = occurences[i][j-1] + 1
            elif (j -1 < 0):
                occurences[i][j] = 0
            else:
                occurences[i][j] = occurences[i][j - 1]

    return array,occurences

def patterMatching(bwtFile, original_string_file, patterns_file):
    """
                This function finds patterns in original string
                :param bwtFile: name of the file to be read
                :param original_string_file: name of the file to be read
                :param patterns_file: name of the file to be read
                :return: Nonde
                :raises: None
                :precondition: valid filenames
                :complexity: best case is O(1) if pattern does'nt exist and worst case is O(M) where m is length of pattern.
                :postcondition: patterns identified
                """

    bwt_string = read_file(bwtFile)
    suffix = []
    for i in range(len(bwt_string)):
        suffix.append(i)

    array, occurences_at_positions = compute_occurences(bwt_string)
    suffixArray, Rank = lf_mapping_to_suffix_array(bwt_string)

    file1 = open(patterns_file, 'r')
    file = open('outputTask3.txt', 'w')

    for item in file1:
        sp = 0
        ep = len(bwt_string) - 1
        pattern = item.strip('\n')
        for i in range(len(pattern) - 1, -1, -1):
            letter = pattern[i]
            rank = Rank[ord(letter)]
            if array[ord(letter)] == None:
                sp = 1
                ep = 0
                break
            elif (sp - 1) < 0:
                nOsp = 0
            else:
                if occurences_at_positions[array[ord(letter)]] == 0:
                    nOsp = 0
                else:
                    nOsp = occurences_at_positions[array[ord(letter)]][sp-1]

            nOep = occurences_at_positions[array[ord(letter)]][ep] - 1
            sp = rank + nOsp
            ep = rank + nOep

        if sp <= ep:
            file.write('The number of occurences for the pattern ' + pattern + ' is ' + str((ep - sp + 1)) + '\n')
            file.write('POSITIONS OF THE PATTERN ' + pattern + ' : ' + '\n')

            sorted_positions = []
            for i in range(sp, ep + 1, 1):
                sorted_positions.append((suffixArray[i]))

            sorted_positions = heap_sort(sorted_positions)
            for i in range(len(sorted_positions)):
                file.write(str(sorted_positions[i]) + '\n')

            file.write('\n')
        else:
            file.write('The pattern ' + pattern + ' does not exist in the original string! ' + 'and has ' + str(
                ep - sp + 1) + ' occurences ' + '\n')
            file.write('\n')







if __name__ == '__main__':
    patterMatching('bwt1000001.txt', 'originalstring.txt', 'shortpatterns2.txt')