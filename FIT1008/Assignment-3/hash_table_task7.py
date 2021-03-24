class QuadraticProbeTable:

    def __init__(self,size=7919):
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
        self.max = 0

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
        b = 250726
        for i in range(len(key)):
            value = (ord(key[i]) + a*value ) % self.table_size
            a = a * b %(self.table_size-1)
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
                if self.max < self.array[position][1]:
                    self.max = self.array[position][1]
                return
            elif self.array[position][0] == key:
                self.array[position] = (key, self.array[position][1]+1)
                if self.max < self.array[position][1]:
                    self.max = self.array[position][1]
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


def frequency(filename):
    """
    This function is used to find to count of each word in the list
    :param alist: List ADT
    :return: True or False depending on the List
    :raises: No exceptions
    :precondition: None
    :complexity: best and worst case is O(n^2) where n is the number of lines in the list
    :postcondtion: None
    """
    text_editor = []

    text_editor = read_file(text_editor,filename)

    if len(text_editor) == 0:
        return False

    words = []
    invalid = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', ']', '[', '/', '?', ';', ':',
               '>', '<', '', ',', '"', '.']
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    for line in range(len(text_editor)):
        Line = text_editor[line]
        string = ''
        for i in range(len(Line)):

            if Line[i].strip() == '.' and ((i - 1) >= 0 and (i + 1) < len(Line)) and (
                        (Line[i - 1]) in numbers) and ((Line[i + 1]) in numbers):
                string = string + Line[i]

            elif Line[i].strip() == '.' and ((i - 1) >= 0 and (i + 1) < len(Line)) and ((Line[i - 1]) == 'i') and (
                        (Line[i + 1]) == 'e'):
                string = string + Line[i]

            elif Line[i].strip() == '.' and ((i - 1) >= 0 and (i + 1) < len(Line)) and ((Line[i - 1]) == 'e') and (
                        (Line[i + 1]) == 'g'):
                string = string + Line[i]

            elif Line[i].strip() not in invalid:
                string = string + Line[i]
                if i + 1 >= len(Line):
                    string = string.lower()
                    words.append(string.strip())
                    string = ''


            elif (Line[i].strip() in invalid) and string != '':
                string = string.lower()
                words.append(string.strip())
                string = ''

    return words

def read_file(templist,filename):
    """
    This function reads line into the list from the file
    :param alist: List ADT
    :param filename: name of the file from which to read lines
    :return:True or False depending on if the file is found or not
    :raises: Assertion error if filename is not a string and FileNotFoundError if file is not found
    :precondition: list and valid filename is entered which exits
    :complexity: best and worst case is O(n) where n is the number of lines in the list
    :postcondition: All the lines of a file are read into the list line by line
    """
    file = open(filename, 'r')

    for line in file:
        line = line.strip('\n')
        templist.append(line)


    file.close()

    return templist

def read_words_into_dictionary(dict,filename):
    """
    This function reads line into the hashtable from the file
    :param dict: hashtable ADT
    :param filename: name of the file from which to read lines
    :return:dict
    :raises: None
    :precondition: hashtable and valid filename is entered which exists
    :complexity: best and worst case is O(n) where n is the number of lines in the list
    :postcondition: All the lines of a file are read into the hash table line by line
    """

    words = frequency(filename)
    for item in words:

        dict[item] = 1

    return len(words)

def find_percentage():
    """
    This function finds the % of the common,uncommon,rare and mispelled words of different users file inputted
    :param None
    :return:None
    :raises: None
    :precondition: None
    :complexity: best and worst case is O(n) where n is the number of files the user enters
    :postcondition: All the percentage of the users files are shown
    """

    dict = QuadraticProbeTable(402221)
    read_words_into_dictionary(dict, 'gutenberg.txt')

    while True:

        try:
            user_input = input('FILE: ')
            words = frequency(user_input)

            common = 0
            uncommon = 0
            rare = 0
            mispelled = 0

            for item in words:

                try:
                    count = dict[item]
                    common_cal = dict.max / 100
                    uncommon_cal = dict.max / 1000

                    if count >= common_cal:
                        common += 1
                    elif count >= uncommon_cal:
                        uncommon += 1
                    else:
                        rare += 1
                except KeyError:
                    mispelled += 1

            print('The percentage of common words is ' + str((100 / len(words)) * common) + '%')
            print('The percentage of uncommon words is ' + str((100 / len(words)) * uncommon) + '%')
            print('The percentage of rare words is ' + str((100 / len(words)) * rare) + '%')
            print('The percentage of mispelled words is ' + str((100 / len(words)) * mispelled) + '%')

        except FileNotFoundError:
            print('?')








if __name__ == '__main__':
    find_percentage()