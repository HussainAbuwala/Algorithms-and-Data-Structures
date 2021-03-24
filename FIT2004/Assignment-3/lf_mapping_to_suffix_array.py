from compute_prefix_sums import rank_bwt

def lf_mapping_to_suffix_array(bwt_string):
    """
                This function performs lf mapping algorithm
                :param filename: filename to be inverted
                :return: None
                :raises: None
                :precondition: valid filename
                :complexity: best and worst case is O(n) where n is the size of the string.
                :postcondition: suffix array and rank returned
                """
    rank,occurences_at_positions = rank_bwt(bwt_string)
    i = 0
    suffix_array = [None] * len(bwt_string)
    suffix_array[0] = len(bwt_string) - 1
    x = len(bwt_string) - 2

    while True:
        letter = bwt_string[i]
        pos = rank[ord(letter)] + occurences_at_positions[i]
        if bwt_string[pos] == '$':
            suffix_array[pos] = 0
            break
        suffix_array[pos] = x
        i = pos
        x-=1

    return suffix_array,rank

if __name__ == '__main__':
    lf_mapping_to_suffix_array('lgo$oo$g')