import csv
import timeit
'''

Although, quadratic probing avoids primary clustering, it still has secondary clustering:
When two keys hash to the same location, they have the same probe sequence.
Since there are only m locations in the table, there are only m possible probe sequences.
One problem with quadratic probing is that probe sequences do not probe all locations in the table.
But since there are (p + 1)/2 quadratic residues when p is prime, we can make the following guarantee.
Claim 2.8. If m is prime and the table is at least half empty, then quadratic probing will always find an empty location.
Furthermore, no locations are checked twice
'''
class QuadraticProbeTable:

    def __init__(self,size=7919,b=27183):
        assert size > 1, "Size should be positive"
        """
        This function automatically creates and array and declares a count variable
        :param size: it is the size of the array to be created by the user
        :return: None
        :raises: Assertion error when size is not an positive integer and when it is >100
        :precondition: size must be a positive integer <=100 and >0
        :complexity: best and worst case is O(n) where n is the size of the array.
        :postcondition: an array of "size = n" is created and count is set to 0
        """
        self.count = 0
        self.array = [None] * size
        self.table_size = size
        self.collisions = 0
        self.b = b

    def __len__(self):
        """
        This function returns the number of items in the hash table
        :param: None
        :return: returns the number of items in the hash table
        :raises: No exceptions
        :precondtion: None
        :postcondition: None
        """
        return self.count

    def hash(self,key):
        assert isinstance(key, str), 'Key can only be string'

        """
        This function calculates the index position at which the (key,data) is to be placed
        :param key: key of which hash value is to be calculated
        :return: None
        :raises: None
        :precondition: key must be string
        :complexity: best and worst case is O(n) where n is the size of the key.
        :postcondition: index position of array is returned
        """
        value = 0
        a = 31415
        for i in range(len(key)):
            value = (ord(key[i]) + a*value ) % self.table_size
            a = a * self.b %(self.table_size-1)
        return value

    def __setitem__(self, key, value):
        """
        This function replaces the key or inserts new key,data pair at position given from hash function
        :param key: position at which a key,data pair is to be placed
        :param value: data to be stored with the key
        :return: None when (key,data) inserted
        :raises: Index error is raised if no space in dictionary
        :precondition: key provided must be string
        complexity: best case is O(1) if key is placed at first position. Worst case is O(n) where key is not after looping through the whole cluster and n is the number of items in dictionary
        :postcondition: (key,data) pair is placed
        """
        position = self.hash(key)
        save = position

        for i in range(self.table_size-1):
            if self.array[position] == None:
                self.array[position] = (key,value)
                self.count+=1
                return
            elif self.array[position][0] == key:
                self.array[position] = (key,value)
                return
            else:
                if self.array[position] != None and i==0 and position == save:
                    self.collisions+= 1
                position = ((save+((i+1)**2)) % self.table_size)

        raise IndexError('No space left in the dictionary')

    def __getitem__(self, key):
        """
        This function finds the data at key given by the user
        :param key: position at which a particular data exists
        :return: the data at position key is returned
        :raises: Key error is raised if key is not found
        :precondition: key provided must be string
        complexity: best case is O(1) if key is found at first position. Worst case is O(n) where key is found after looping through the whole cluster and n is the number of (key,data) pairs in the hash table.
        :postcondition: item is found at valid key and dat returned to user
        """
        position = self.hash(key)
        save = position

        for i in range(self.table_size-1):
            if self.array[position] == None:
                raise KeyError('KEY NOT FOUND')
            elif self.array[position][0] == key:
                return self.array[position][1]
            else:
                position = ((save + ((i+1) ** 2)) % self.table_size)

        raise KeyError('KEY NOT FOUND')

    def __contains__(self, key):
        """
        This function checks if key exists in the array
        :param key: key the user wants to see if its in list
        :return: True or False depending if key exists or not
        :raises: No exceptions
        :precondtion: an key must be provided as parameter to find
        :complexity: best case is O(1) if item is found in first position and worst case is O(n) where n is the number of items in the array and item is found at last or not found
        :postcondition: True or false is returned if precondtion is met
        """
        position = self.hash(key)
        save = position

        for i in range(self.table_size-1):
            if self.array[position] == None:
                return False
            elif self.array[position][0] == key:
                return True
            else:
                position = ((save + ((i+1) ** 2)) % self.table_size)

        return False

    def __str__(self):
        """
        This function returns the string representation of the list
        :param: None
        :return: returns string represenation of list with each item in new line
        :raises: no exceptions
        :precondition: No precondition
        :complexity: best case and worst case is O(n) where n is the number of items in the list
        :postcondition: a string representation of list is made
        """
        result = '{'

        for item in self.array:
            if item != None:
                (key,value) = item
                result = result + '' + str(key) + ':' + ' ' + str(value) + ',' + ' '

        result+= '}'
        return result

def read_time_sum_insertion(hashtable,filename):
    """
    This function reads line into the hashtable from the file and calculates time
    :param hashtable: hashtable ADT
    :param filename: name of the file from which to read lines
    :return:time taken to read file
    :raises: None
    :precondition: hashtable and valid filename is entered which exists
    :complexity: best and worst case is O(n) where n is the number of lines in the file
    :postcondition: All the lines of a file are read into the hashtable line by line
    """
    file = open(filename, 'r')
    start = timeit.default_timer()

    for line in file:
        line = line.strip('\n')
        hashtable[line] = line

    taken = (timeit.default_timer() - start)
    file.close()

    return taken

def find_all_combinations():#500057,1000151
    """
    This function finds all combinations of data
    :param None
    :return:None
    :raises: None
    :precondition: None
    :complexity: best and worst case is O(n) where n is the total combinations
    :postcondition: data collected
    """

    filenames = ['english_large.txt','english_small.txt','french.txt']
    values = [['b', 'table_size', 'time','collisions']]
    for filename in filenames:


        dict = QuadraticProbeTable(250727, 1)
        time = read_time_sum_insertion(dict, filename)
        values.append([1,250727,time,dict.collisions])

        dict = QuadraticProbeTable(402221, 1)
        time = read_time_sum_insertion(dict, filename)
        values.append([1, 402221, time,dict.collisions ])

        dict = QuadraticProbeTable(700001, 1)
        time = read_time_sum_insertion(dict, filename)
        values.append([1, 700001, time,dict.collisions])

        dict = QuadraticProbeTable(1000081, 1)
        time = read_time_sum_insertion(dict, filename)
        values.append([1, 1000081, time,dict.collisions])

        dict = QuadraticProbeTable(2000003, 1)
        time = read_time_sum_insertion(dict, filename)
        values.append([1, 2000003, time,dict.collisions])

        dict = QuadraticProbeTable(5000011, 1)
        time = read_time_sum_insertion(dict, filename)
        values.append([1, 5000011, time,dict.collisions])

        dict = QuadraticProbeTable(250727, 27183)
        time = read_time_sum_insertion(dict, filename)
        values.append([27183, 250727, time,dict.collisions])

        dict = QuadraticProbeTable(402221, 27183)
        time = read_time_sum_insertion(dict, filename)
        values.append([27183, 402221, time,dict.collisions])

        dict = QuadraticProbeTable(700001, 27183)
        time = read_time_sum_insertion(dict, filename)
        values.append([27183, 700001, time,dict.collisions])

        dict = QuadraticProbeTable(1000081, 27183)
        time = read_time_sum_insertion(dict, filename)
        values.append([27183, 1000081, time,dict.collisions])

        dict = QuadraticProbeTable(2000003, 27183)
        time = read_time_sum_insertion(dict, filename)
        values.append([27183, 2000003, time,dict.collisions])

        dict = QuadraticProbeTable(5000011, 27183)
        time = read_time_sum_insertion(dict, filename)
        values.append([27183, 5000011, time,dict.collisions])

        dict = QuadraticProbeTable(402221, 250726)
        time = read_time_sum_insertion(dict, filename)
        values.append([250726, 402221, time,dict.collisions])

        dict = QuadraticProbeTable(700001, 250726)
        time = read_time_sum_insertion(dict, filename)
        values.append([250726, 700001, time,dict.collisions])

        dict = QuadraticProbeTable(1000081, 250726)
        time = read_time_sum_insertion(dict, filename)
        values.append([250726, 1000081, time,dict.collisions])

        dict = QuadraticProbeTable(2000003, 250726)
        time = read_time_sum_insertion(dict, filename)
        values.append([250726, 2000003, time,dict.collisions])

        dict = QuadraticProbeTable(5000011, 250726)
        time = read_time_sum_insertion(dict, filename)
        values.append([250726, 5000011, time,dict.collisions])

        dict = QuadraticProbeTable(250727, 500057)
        time = read_time_sum_insertion(dict, filename)
        values.append([500057, 250727, time,dict.collisions])

        dict = QuadraticProbeTable(402221, 500057)
        time = read_time_sum_insertion(dict, filename)
        values.append([500057, 402221, time,dict.collisions])

        dict = QuadraticProbeTable(700001, 500057)
        time = read_time_sum_insertion(dict, filename)
        values.append([500057, 700001, time,dict.collisions])

        dict = QuadraticProbeTable(1000081, 500057)
        time = read_time_sum_insertion(dict, filename)
        values.append([500057, 1000081, time,dict.collisions])

        dict = QuadraticProbeTable(2000003, 500057)
        time = read_time_sum_insertion(dict, filename)
        values.append([500057, 2000003, time,dict.collisions])

        dict = QuadraticProbeTable(5000011, 500057)
        time = read_time_sum_insertion(dict, filename)
        values.append([500057, 5000011, time,dict.collisions])

        dict = QuadraticProbeTable(250727, 1000151)
        time = read_time_sum_insertion(dict, filename)
        values.append([1000151, 250727, time,dict.collisions])

        dict = QuadraticProbeTable(402221, 1000151)
        time = read_time_sum_insertion(dict, filename)
        values.append([1000151, 402221, time,dict.collisions])

        dict = QuadraticProbeTable(700001, 1000151)
        time = read_time_sum_insertion(dict, filename)
        values.append([1000151, 700001, time,dict.collisions])

        dict = QuadraticProbeTable(1000081, 1000151)
        time = read_time_sum_insertion(dict, filename)
        values.append([1000151, 1000081, time,dict.collisions])

        dict = QuadraticProbeTable(2000003, 1000151)
        time = read_time_sum_insertion(dict, filename)
        values.append([1000151, 2000003, time,dict.collisions])

        dict = QuadraticProbeTable(5000011, 1000151)
        time = read_time_sum_insertion(dict, filename)
        values.append([1000151, 5000011, time,dict.collisions])



        if filename != 'french.txt':
            values.append(['b', 'table_size', 'time','collisions'])



    csv_writer(values)#5#

def csv_writer(n_time):
    """
    This function writes data into csv file
    :param n_time: data to write
    :return:None
    :raises: None
    :precondition: data to be written provided
    :complexity: best and worst case is O(n) where n is the number of data in the file
    :postcondition: All data write to csv
    """
    with open('task4.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)

        for i in range(len(n_time)):
            spamwriter.writerow([n_time[i][0],n_time[i][1],n_time[i][2],n_time[i][3]])


def unicode_values_strings():

    characters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o'
                  ,'p','q','r','s','t','u','v','w','x','y','z']

    capital = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O'
                  ,'P','Q','R','S','T','U','V','W','X','Y','Z']
    for chr in characters:
        print('CODE OF ' + str(chr) + ' =   ' + str(ord(chr)))

    print('--------------------------------------')

    for chr in capital:
        print('CODE OF ' + str(chr) + ' =   ' + str(ord(chr)))

if __name__ == '__main__':
    find_all_combinations()




