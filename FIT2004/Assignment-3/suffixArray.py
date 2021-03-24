def rank(previous_rank,sIndex,jump):
    """
            This function finds the rank
            :param previous_rank: previous rank
            :param sIndex: list to be sorted
            :param jump: jumping
            :return: rank
            :raises: None
            :precondition: valid paramters
            :complexity: best and worst case is O(N).
            :postcondition: rank returned
            """
    number = 0
    temp = [None] * len(sIndex)
    check = False
    for i in range(0,len(sIndex)):

        if (i + 1) == len(sIndex):
            temp[sIndex[i]] = number

        else:
            sIndex1 = sIndex[i]
            sIndex2 = sIndex[i + 1]
            if (suffix_compare(previous_rank , sIndex1, sIndex2,jump) == 0):
                temp[sIndex[i]] = number
                number+=1
            elif (suffix_compare(previous_rank , sIndex1, sIndex2,jump) == -1):
                temp[sIndex[i]] = number
                check = True

    if check == False:
        return check
    return temp

def suffix_compare(previous_rank , sIndex1, sIndex2,jump):

    """
            This function compares
            :param previous_rank: previous rank
            :param sIndex1: first item to be compared
            :param sIndex2: first compared
            :param jump: jumping
            :return: result
            :raises: None
            :precondition: valid paramters
            :complexity: best and worst case is O(1).
            :postcondition: 0/1/-1 returned
            """
    
    if (previous_rank[sIndex1] < previous_rank[sIndex2]):
        return 0
    elif (previous_rank[sIndex2] < previous_rank[sIndex1]):
        return 1
    elif (previous_rank[sIndex1] == previous_rank[sIndex2]):
        sIndex1 = sIndex1 + jump
        sIndex2 = sIndex2 + jump

        if sIndex1 >= len(previous_rank) and sIndex2 < len(previous_rank):
            return 0
        elif sIndex2 >= len(previous_rank) and sIndex1 < len(previous_rank):
            return 1
        elif previous_rank[sIndex1] < previous_rank[sIndex2]:
            return 0
        elif (previous_rank[sIndex2] < previous_rank[sIndex1]):
            return 1
        else:
            return -1









