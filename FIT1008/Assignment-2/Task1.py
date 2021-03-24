class List:

    def __init__(self, size=100):
        """
        This function automatically creates and array and declares a count variable
        :param size: it is the size of the array to be created by the user
        :return: None
        :raises: Assertion error when size is not an positive integer and when it is >100
        :precondition: size must be a positive integer <=100 and >0
        :complexity: best and worst case is O(n) where n is the size of the array.
        :postcondition: an array of "size = n" is created and count is set to 0
        """
        assert isinstance(size,int),"Only integer input allowed"
        assert size > 0, "Size should be positive"
        assert size >0 and size<=100, "Size out of range(Size valid from 1-100 inclusive)"
        self.array = size * [None]
        self.count = 0

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
        string = '"'
        for i in range(self.count):
            if i == self.count-1:
                string = string + str(self.array[i]) + '"'
            else:
                string = string + str(self.array[i]) + '\n '

        if self.count== 0:
            string = '""'
            return string

        return string

    def __len__(self):
        """
        This function returns the number of items in the list
        :param: None
        :return: returns the number of items in the list
        :raises: No exceptions
        :precondtion: None
        :postcondition: None
        """
        return self.count

    def __contains__(self, item):
        """
        This function checks if item exists in the list
        :param item: item the user wants to see if its in list
        :return: True or False depending if item exists or not
        :raises: No exceptions
        :precondtion: an item must be provided as parameter to find
        :complexity: best case is O(1) if item is found in first position and worst case is O(n) where n is the number of items in the list and item is found at last or not found
        :postcondition: True or false is returned if precondtion is met
        """
        for j in range(self.count):
            if item == self.array[j]:
                return True

        return False

    def __getitem__(self, index):
        """
        This function finds the item at index given by the user
        :param index: position at which a particular item exists
        :return: the item at position index is returned
        :raises: Assertion error is raised if index is not an integer and IndexError is raised if index is out of range
        :precondition: index provided must be positive integer in the range >=0 and <count
        complexity: best case and worst case is O(1) as it takes constant time to access any position in the array.
        :postcondition: item is found at valid index and returned to user
        """
        assert isinstance(index, int), "Only integer input allowed"
        if index <0 or index>= self.count:
            raise IndexError

        return self.array[index]

    def __setitem__(self, key, value):
        """
        This function replaces the item at index given by the user with the key given by user
        :param key: position at which a particular item exists
        :param value: item to replace with another item at position key
        :return: True when item is replaced
        :raises: Assertion error is raised if key is not an integer and IndexError is raised if key is out of range
        :precondition: key provided must be positive integer in the range >=0 and <count
        complexity: best case and worst case is O(1) as it takes constant time to access any position in the array.
        :postcondition: item is set at valid index given by user
        """
        assert isinstance(key, int), "Only integer input allowed"
        if key <0 or key>= self.count:
            raise IndexError

        self.array[key] = value

        return True


    def __eq__(self, other):

        """
        This function checks if two lists are equal to each other in terms of item
        :param other:List to check with our ADT list array
        :return: True or False depending on if both lists are equal
        :raises: Assertion error if other is not a list class
        precondition: a list is given a parameter
        :complexity:best case is O(1) if both list do not have the same number of items and worst case is O(n) where n is the number of items in the list
        :postcondition: both lists are checked and True or False is returned after checking
        """
        assert isinstance(other,(list,List)),"Only List input is allowed"
        if len(other) != self.count:
            return False

        check = True
        for i in range(len(other)):
            if other[i]!= self.array[i]:
                check = False

        return check

    def is_empty(self):
        """
        This function checks if the array is empty
        :param: none
        :return: returns True or False depending on if list is empty or not
        :raises: No exceptions
        :preconditions: None
        :complexity: best and worst case is O(1)
        :postcondition: None
        """
        return self.count == 0

    def is_full(self):
        """
        This function checks if the array is full
        :param: none
        :return: returns True or False depending on if list is full or not
        :raises: No exceptions
        :preconditions: None
        :complexity: best and worst case is O(1)
        :postcondition: None
        """
        return self.count >= len(self.array)

    def append(self,item):
        """
        This function adds item to the end of the list
        :param item: the item to add at the end of the list
        :return: True or false depending on if item is added to end of list or not
        :raises: No exceptions
        :precondition: item must be given as paramter to add to end of list
        :complexity: best case and worst case is O(1)
        :postcondition: item is added at end of list if list not full
        """
        has_space_left = not self.is_full()
        if has_space_left:
            self.array[self.count] = item
            self.count += 1
        return has_space_left

    def insert(self,index,item):
        """
        This function places item at given index by the user and shifting other items
        :param index: position to place item before
        :param item: item to insert at position
        :return: True or False depending on if item is inserted or not
        :raises: Assertion error is raised if index is not an integer and IndexError is raised if index is out of range
        :complexity: best case is 0(1) if item is inserted at the end of the list and worst case is O(n) if item is inserted at first index
        :precondition: valid index must be entered and a item must be given as parameter
        :postcondition: item inserted at valid index
        """
        assert isinstance(index, int), "Only integer input allowed"
        if index <0 or index> self.count:
            raise IndexError

        if self.is_full():
            return False

        if index== self.count:
            self.append(item)
            return True
        else:
            for i in range(self.count-1,index-1,-1):
                self.array[i+1] = self.array[i]

            self.array[index] = item
            self.count+= 1
            return True

    def remove(self,item):
        """
        This function removes the first instance of the item from the list
        :param item: item to remove from the list
        :return: returns True is item is removed
        :raises: Assertion error if list is empty and ValueError if item not found
        :precondition: item provided must be in the list
        complexity: best case and worst case is O(n) where n is the number of items in the list
        :postcondition: first instance of item is removed.
        """
        assert not self.is_empty(),'Cannot remove an item from empty list'
        
        found = False
        for i in range(self.count):
            if self.array[i]==item:
                found = True
                index = i
                break

        if found == False:
            raise ValueError

        for j in range(index+1,self.count):
            self.array[j-1] = self.array[j]

        self.count-= 1
        return True

    def delete(self, index):
        """
        This function deletes the item at the given index by the user
        :param index: position at which the item is present to delete
        :return: True is item at index is deleted
        :raises: Assertion error if index is not integer and Indexerror if index is out of range
        :precondition: valid index is provided
        :complexity: best case is O(1) if index to be deleted is the last item and worst case is O(n) if item to be deleted is at index 0
        :postcondition: item is deleted at valid index
        """
        assert isinstance(index, int), "Only integer input allowed"
        if index < 0 or index >= self.count:
            raise IndexError

        for i in range(index, self.count-1):
            self.array[i] = self.array[i+1]
        self.count -=1

        return True


if __name__ == '__main__':

    my_list = List(5)
    print(str(my_list))
    print(len(my_list))
    my_list.append('a')
    print(str(my_list))
    print(len(my_list))
    my_list.append('b')
    print(str(my_list))
    print(len(my_list))
    my_list.insert(0,'c')
    print(str(my_list))
    print(len(my_list))
    print(my_list == ['c','a','b'])
    print('c' in my_list)
    print('x' in my_list)
    print(my_list[1])
    my_list[2] = 'z'
    print(str(my_list))
    my_list.remove('a')
    print(my_list)
    print(len(my_list))
    my_list.delete(1)
    print(my_list)
    print(len(my_list))






