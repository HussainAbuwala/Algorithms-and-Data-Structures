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
        self.markers = 0

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
        hash = 0

        for i in range(1, len(key) + 1):
            hash += ord(key[i - 1]) * (26 ** (len(key) - i))

        return (hash % self.table_size)

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

        load_factor = self.count / self.table_size
        if load_factor >= 0.5:
            new_size = (self.table_size * 2) + 1
            self.rehash(new_size)

        self._setitem_aux(key,value)

        load_factor = self.count / self.table_size
        if load_factor >= 0.5:
            new_size = (self.table_size * 2) + 1
            self.rehash(new_size)

        return

    def _setitem_aux(self,key,value):
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

        check = True
        for i in range(self.table_size - 1):
            if self.array[position] == None and check == True:
                self.array[position] = (key, value)
                self.count += 1
                return

            elif self.array[position] == None and check == False:
                self.array[copy] = (key, value)
                self.count += 1
                self.markers -= 1
                return

            elif self.array[position][0] == key:
                self.array[position] = (key, value)
                return
            else:

                if self.array[position] == 'DELETED' and check == True:
                    check = False
                    copy = position

                position = ((save + ((i + 1) ** 2)) % self.table_size)

        if check == False:
            self.array[copy] = (key, value)
            self.count += 1
            self.markers -= 1
            return

        raise IndexError('No space left in the dictionary')

    def delete(self,key):
        """
        This function checks deletes key from the hashtable
        :param key: key the user wants to remove
        :return: None
        :raises: KeyError if key not found
        :precondtion: an key must be provided as parameter to delete
        :complexity: best case is O(1) if item is found in first position and worst case is O(n) where n is the number of items in the array and item is found at last or not found
        :postcondition: item deleted
        """
        self._delete_aux_(key)

        if (self.markers / self.table_size) >= 0.5:
            self.rehash(self.table_size)

        return

    def _delete_aux_(self,key):
        """
        This function checks deletes key from the hashtable
        :param key: key the user wants to remove
        :return: None
        :raises: KeyError if key not found
        :precondtion: an key must be provided as parameter to delete
        :complexity: best case is O(1) if item is found in first position and worst case is O(n) where n is the number of items in the array and item is found at last or not found
        :postcondition: item deleted
        """
        position = self.hash(key)
        save = position

        for i in range(self.table_size-1):
            if self.array[position] == None:
                raise KeyError('KEY NOT FOUND')
            elif self.array[position][0] == key:
                self.array[position] = 'DELETED'
                self.markers += 1
                self.count-=1
                return
            else:
                position = ((save+((i+1)**2)) % self.table_size)

        raise KeyError('KEY NOT FOUND')

    def rehash(self,tablesize):

        """
        This function changes the size of the table
        :param tablesize: size to which hashtable is increases
        :return: None
        :raises: No exceptions
        :precondtion: an tablesize must be provided as parameter to increase size
        :complexity: best case and worst case is O(n) where n is the number of items in the array to be rehashed
        :postcondition: table size increased and all it items succesfully added in new table
        """
        if tablesize == self.table_size:
            new_array = self.array

            self.array = [None] * tablesize
            self.count = 0
            self.markers = 0

            for item in new_array:
                if item!= None and item!= 'DELETED':
                    self._setitem_aux(item[0],item[1])

            return

        else:

            new_array = self.array

            self.array = [None] * tablesize
            self.count = 0
            self.table_size = tablesize
            self.markers = 0

            for item in new_array:
                if item != None and item != 'DELETED':
                    self._setitem_aux(item[0], item[1])


            return

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


if __name__ == '__main__':
    dict = QuadraticProbeTable(7)
    dict['HUSSAIN'] = 'mama'
    dict.delete('HUSSAIN')
    dict.delete('MAMA')

    '''dict['SADIQ'] = 'GABRU'
    print(dict.array)
    dict.delete('SADIQ')
    print(dict.array)
    print(dict.markers)
    print(dict.count)
    print(dict.table_size)'''
