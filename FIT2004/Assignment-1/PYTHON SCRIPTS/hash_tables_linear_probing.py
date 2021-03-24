class LinearProbeTable:

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
        assert size > 1, "Size should be positive"
        self.count = 0
        self.array = [None] * size
        self.table_size = size

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
        assert isinstance(key,str), 'Key can only be string'
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
        a = 31415           #a = MULTIPLIER
        b = 27183
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

        for _ in range(self.table_size):
            if self.array[position] == None:
                self.array[position] = (key,value)
                self.count+=1
                return
            elif self.array[position][0] == key:
                self.array[position] = (key,self.array[position][1] + 1)
                return
            else:
                position = (position+1) % self.table_size

        raise IndexError('No space left in the dictionary')

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
        for _ in range(self.table_size):
            if self.array[position] == None:
                return False
            elif self.array[position][0] == key:
                return True
            else:
                position = (position + 1) % self.table_size

        return False



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

        for _ in range(self.table_size):
            if self.array[position] == None:
                raise KeyError('KEY NOT FOUND')
            elif self.array[position][0] == key:
                return self.array[position][1]
            else:
                position = (position + 1) % self.table_size

        raise KeyError('KEY NOT FOUND')

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