class cuckooHashing:

    def __init__(self,size=4000):

        """
                This function automatically creates and array and declares a count variable
                :param size: it is the size of the array to be created by the user
                :return: None
                :raises: None
                :precondition: size must be a positive integer
                :complexity: best and worst case is O(n) where n is the size of the array.
                :postcondition: an array of "size = n" is created.
                """

        self.table1 = [None] * size
        self.table2 = [None] * size
        self.tablesize = size

    def hash_function_one(self,string):

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

        for i in range(1,len(string)+1):
            hash += ord(string[i-1]) * (26 ** (len(string) - i))

        return hash % self.tablesize

    def hash_function_two(self,string):

        """
                This function calculates the index position at which the (key,data) is to be placed
                :param key: key of which hash value is to be calculated
                :return: None
                :raises: None
                :precondition: key must be string
                :complexity: best and worst case is O(n) where n is the size of the key.
                :postcondition: index position of array is returned
                """

        h = 0

        for i in range(len(string)):
            h = (33 * h) + ord(string[i])

        return h % self.tablesize

    def __setitem__(self, key, value):

        """
                This function replaces the key or inserts new key,data pair at position given from hash function
                :param key: position at which a key,data pair is to be placed
                :param value: data to be stored with the key
                :return: None when (key,data) inserted
                :raises: Index error is raised if no space in dictionary
                :precondition: key provided must be string
                complexity: best case is O(1) if key is placed at first position else amortized O(n)
                :postcondition: (key,data) pair is placed
                """

        index = self.hash_function_one(key)
        copy = self.table1
        save = (key,value)

        infinit_check_index = index
        infinit_check_key = key


        while True:

            if (copy == self.table1):
                if copy[index] == None:
                    copy[index] = save
                    return

                elif copy[index][0] == save[0]:
                    copy[index] = save
                    return
                else:
                    old = copy[index]
                    copy[index] = save
                    save = old
                    index = self.hash_function_two(save[0])

                    if (index == infinit_check_index and save[0] == infinit_check_key):
                        break
                    copy = self.table2
            else:
                if copy[index] == None:
                    copy[index] = save
                    return

                elif copy[index][0] == save[0]:
                    copy[index] = save
                    return
                else:
                    old = copy[index]
                    copy[index] = save
                    save = old
                    index = self.hash_function_one(save[0])

                    if (index == infinit_check_index and save[0] == infinit_check_key):
                        break
                    copy = self.table1

        self.rehash(key,value)

    def __getitem__(self, key):

        """
                This function finds the data at key given by the user
                :param key: position at which a particular data exists
                :return: the data at position key is returned
                :raises: Key error is raised if key is not found
                :precondition: key provided must be string
                complexity: best case is O(1) if key is found at first position. Worst case is O(n) where key is found after looping through the whole cluster and n is the number of (key,data) pairs in the hash table.
                :postcondition: item is found at valid key and is returned to user
                """
        
        h1 = self.hash_function_one(key)
        if self.table1[h1] != None and self.table1[h1][0] == key:
            return self.table1[h1][1]
        h2 = self.hash_function_two(key)
        if self.table2[h2] != None and self.table2[h2][0] == key:
            return self.table2[h2][1]
        raise KeyError('Key not found')

    def delete(self,key):

        """
                This function checks deletes key from the hashtable
                :param key: key the user wants to remove
                :return: None
                :raises: KeyError if key not found
                :precondtion: an key must be provided as parameter to delete
                :complexity: best case and worst case is O(1)
                """

        h1 = self.hash_function_one(key)
        if self.table1[h1]!= None and self.table1[h1][0] == key:
            self.table1[h1] = None
            return
        h2 = self.hash_function_two(key)
        if self.table2[h2] != None and self.table2[h2][0] == key:
            self.table2[h2] = None
            return
        raise KeyError('Key not found')

    def rehash(self,key,value):

        """
                This function changes the size of the table
                :param key: which could not be inserted
                :param value: which could not be inserted
                :return: None
                :raises: No exceptions
                :precondtion: key and value provided
                :complexity: best case and worst case is O(n) where n is the number of items in the array to be rehashed
                :postcondition: table size increased and all it items succesfully added in new table
                """

        self.tablesize = self.tablesize * 2
        array1 = self.table1
        array2 = self.table2

        self.table1 = [None] * self.tablesize
        self.table2 = [None] * self.tablesize

        for item in array1:
            if item != None:
                self.__setitem__(item[0], item[1])

        for item in array2:
            if item != None:
                self.__setitem__(item[0], item[1])

        self.__setitem__(key,value)

    def __contains__(self, key):

        """
                This function checks if key exists in the array
                :param key: key the user wants to see if its in list
                :return: True or False depending if key exists or not
                :raises: No exceptions
                :precondtion: an key must be provided as parameter to find
                :complexity: best case and worst case is O(1)
                :postcondition: True or false is returned if precondtion is met
                """

        h1 = self.hash_function_one(key)
        if self.table1[h1] != None and self.table1[h1][0] == key:
            return True
        h2 = self.hash_function_two(key)
        if self.table2[h2] != None and self.table2[h2][0] == key:
            return True
        return False


if __name__ == '__main__':
    hashtable = cuckooHashing()

    hashtable['HUSSAIN'] = 1
    print(hashtable.table1)
    print(hashtable.table2)

    hashtable['TASIN'] = 1
    print(hashtable.table1)
    print(hashtable.table2)

    hashtable['MARK'] = 1
    print(hashtable.table1)
    print(hashtable.table2)

    hashtable['SODA'] = 1
    print(hashtable.table1)
    print(hashtable.table2)

    hashtable['SOD'] = 1
    print(hashtable.table1)
    print(hashtable.table2)

    hashtable['SODw'] = 1
    print(hashtable.table1)
    print(hashtable.table2)

    hashtable['SODq'] = 1
    print(hashtable.table1)
    print(hashtable.table2)

    '''hashtable.delete('HUSSAIN')
    print(hashtable.table1)
    print(hashtable.table2)

    hashtable.delete('SODA')
    print(hashtable.table1)
    print(hashtable.table2)'''



