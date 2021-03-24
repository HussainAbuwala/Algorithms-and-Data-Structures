from heap import*
from hash_table_task8 import QuadraticProbeTable

def frequencies(filename):
    """
        This function calcuates frequencies of each word
        :param filename: file to read
        :return: None
        :raises: None
        :precondition: valid filename
        :complexity: best and worst case is O(n) where n is the number of lines in the file.
        :postcondition: words with its written to 'FREQUENCY.txt'
        """

    hashtable = QuadraticProbeTable()
    file = open(filename,'r')
    words = []

    for item in file:
        item = item.strip('\n')
        if item not in hashtable:
            hashtable[item] = 1
            words.append(item)
        else: hashtable[item] = hashtable[item] + 1

    file = open('FREQUENCY.txt', 'w')
    words = heap_sort(words)
    for item in words: file.write(item + ' ' + str(hashtable[item]) + '\n')


frequencies('splitwords.txt')