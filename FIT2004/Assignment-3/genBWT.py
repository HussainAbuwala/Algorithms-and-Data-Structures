from suffixArray import rank
from suffixArray import suffix_compare


def mergeSort(alist,rank,jump):
    """
            This function sorts based on rank of suffixes
            :param alist: list to sort
            :param rank: associated ranks
            :param jump: value to jump
            :return: sorted list
            :raises: None
            :precondition: valid parametes
            :complexity: best and worst case is O(nlogn) where n is the number of keys.
            :postcondition: sorted list found
            """
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf,rank,jump)
        mergeSort(righthalf,rank,jump)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):

            value = suffix_compare(rank,lefthalf[i],righthalf[j],jump)
            if value == 0 or value == -1:
                alist[k] = lefthalf[i]
                i = i + 1
            else:
                alist[k] = righthalf[j]
                j = j + 1
            k = k + 1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1

        return alist

def computeSuffixArray (sIndex,string):
    """
            This function finds the suffix array
            :param sINDEX: list
            :param string: original string
            :return: sIndex
            :raises: None
            :precondition: valid parametes
            :complexity: best and worst case is O(nlog^2n) where n is the number of keys.
            :postcondition: suffix array computed
            """
    previous_rank = rankOfFirstCharacter(sIndex,string)
    sIndex = counting_sort(sIndex,string)

    i = 2
    x = 0
    while i < len(sIndex):
        sIndex = mergeSort(sIndex,previous_rank,2 ** x)
        new_rank = rank(previous_rank, sIndex, 2 ** x)
        if new_rank == False:
            break
        previous_rank = new_rank
        x = x + 1
        i = 2 * i

    return sIndex

def rankOfFirstCharacter(sIndex,string):
    """
            This function finds the rank of the first character
            :param sIndex: list
            :param string: original string
            :return: rank
            :raises: None
            :precondition: valid parametes
            :complexity: best and worst case is O(n) where n is the len of string.
            :postcondition: rank found
            """

    rank = [None] * len(sIndex)

    for i in range (len(sIndex)):
        rank[i] = ord(string[sIndex[i]])

    return rank

def computeBWT(filename):
    """
            This function finds the bwt string
            :param filename: name of file
            :return: None
            :raises: None
            :precondition: valid parametes
            :complexity: best and worst case is O(nlon^2n) where n is the number of keys.
            :postcondition: bwt written to file
            """

    file = open(filename, "r")
    string = file.readline().strip('\n')

    suffix = []
    for i in range(len(string)):
        suffix.append(i)

    sortedSuffix = computeSuffixArray(suffix,string)

    bwt_string = ''

    for item in sortedSuffix:
        if (item -1 < 0):
            bwt_string = bwt_string + '$'
        else:
            bwt_string = bwt_string + string[item-1]

    file = open('outputBWT.txt','w')
    file.write(bwt_string)

def counting_sort(items,string):
    """
            This function finds sorted list by first character
            :param items: list
            :param string: original string
            :return: sorted list
            :raises: None
            :precondition: valid parametes
            :complexity: sorted by first character
            """
    new_array = [0] * (256)

    for i in range(len(items)):
        new_array[ord(string[items[i]])] += 1

    for i in range(1,len(new_array)):
        new_array[i] = new_array[i] + new_array[i-1]

    sorted_array = [0] * len(items)

    for i in range(len(items)-1 , -1, -1):
        new_array[ord(string[items[i]])] -= 1
        sorted_array[new_array[ord(string[items[i]])]] = items[i]

    return sorted_array

if __name__ == '__main__':
    computeBWT(input())