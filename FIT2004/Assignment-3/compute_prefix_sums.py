def rank_bwt(string):
    """
                This function finds rank and occurences
                :param string: string
                :return: rank and occurences
                :raises: None
                :precondition: valid string
                :complexity: best and worst case is O(n) where n is the size of the string.
                :postcondition: rank and occurences returned
                """

    occurences = [0] * (256)
    positions = [0] * len(string)

    for i in range(len(string)):
        positions[i] = occurences[ord(string[i])]
        occurences[ord(string[i])] += 1

    prefix_sums = [0] * 256

    for i in range(1,len(prefix_sums)):
        prefix_sums[i] = prefix_sums[i-1] + occurences[i]

    rank = [0] * 256
    for i in range(len(string)):
            rank[ord(string[i])] = prefix_sums[ord(string[i])] - occurences[ord(string[i])]

    return rank,positions

