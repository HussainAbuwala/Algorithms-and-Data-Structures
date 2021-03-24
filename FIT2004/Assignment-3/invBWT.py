from compute_prefix_sums import rank_bwt

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

    # read_file
    file = open(filename, "r")
    bwt_string = file.readline().strip('\n')
    return bwt_string

def lf_mapping(filename):
    """
            This function performs lf mapping algorithm
            :param filename: filename to be inverted
            :return: None
            :raises: None
            :precondition: valid filename
            :complexity: best and worst case is O(n) where n is the size of the string.
            :postcondition: contents written to file
            """
    bwt_string = read_file(filename)
    rank,occurences_at_positions = rank_bwt(bwt_string)

    i = 0
    string = bwt_string[0] + '$'

    while True:
        letter = bwt_string[i]
        pos = rank[ord(letter)] + occurences_at_positions[i]
        if bwt_string[pos] == '$':
            break
        string = bwt_string[pos] + string
        i = pos

    write_to_file('originalstring.txt',string)

def write_to_file(filename,string):
    """
            This function writes string to a file
            :param filename: name of the file where contents will be written to
            :param string: string
            :return: None
            :raises: None
            :precondition: valid filename
            :complexity: best and worst case is O(1).
            :postcondition: contents written to file
            """
    # write to file
    file = open(filename, 'w')
    file.write(string)

if __name__ == '__main__':
    lf_mapping(input())