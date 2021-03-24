import sys
import re
import os

class Stack:
    def __init__(self, size=100):
        """
        This function automatically creates and array and declares a count variable and size variable and top variable
        :param size: it is the size of the array to be created by the user
        :return: None
        :raises: Assertion error when size is not an positive integer >0
        :precondition: size must be a positive integer >0
        :complexity: best and worst case is O(n) where n is the size of the array.
        :postcondition: an array of "size = n" is created and count is set to 0
        """
        assert isinstance(size,int),"Only integer input allowed"
        assert size > 0, "Size should be positive and >0"
        self.array = size * [None]
        self.count = 0
        self.array_size = size
        self.top = -1

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
            string = '" "'
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

    def push(self,item):
        """
        This function pushes item at the top of the stack
        :param item: item to be pushed on the stack
        :return: True when the item is pushed on the stack
        :raises: No exceptions
        :preconditions: item must be provided to be pushed
        :complexity: O(1) is stack is not full and O(n) if stack is full
        :postconditions: item is pushed on the top of the stack
        """
        has_space_left = self.is_full()
        if has_space_left == False:
            self.top+=1
            self.array[self.top] = item
            self.count += 1
            return True
        else:
            temp = []
            while self.is_empty()!= True:
                temp.append(self.pop())

            self.array = [None] * self.array_size * 10
            self.array_size = self.array_size * 10
            self.count = 0
            self.top = -1

            for i in range(len(temp)-1,-1,-1):
                self.top+=1
                self.array[self.top] = temp[i]
                self.count += 1

            self.top += 1
            self.array[self.top] = item
            self.count += 1
            return True

    def pop(self):
        """
        This function pops item at the top of the stack
        :param item: item to be popped from the stack
        :return: item when validly popped
        :raises: Assertion error when stack is empty
        :preconditions: stack should not be empty
        :complexity: best and worst case is 0(1)
        :postconditions: item is popped from the top of the stack
        """
        assert not self.is_empty(), "Stack is empty"
        item = self.array[self.top]
        self.top -= 1
        self.count -=1
        return item

    def peek(self):
        """
        This function looks item at the top of the stack
        :param None
        :return: item at top of stack
        :raises: Assertion error when stack is empty
        :preconditions: stack should not be empty
        :complexity: best and worst case is 0(1)
        :postconditions: item is popped from the top of the stack
        """
        assert not self.is_empty(), "Stack is empty"
        item = self.array[self.top]
        return item

    def reset(self):
        """
        The stack is made to be empty
        :return: None
        :param: None
        :raises: No exceptions
        :complexity: O(1) for best and worst case
        :preconditions: None
        :postconditions: None
        """
        self.count = 0
        self.top = -1


class List:

    def __init__(self, size=100):
        """
        This function automatically creates and array and declares a count variable and size variable
        :param size: it is the size of the array to be created by the user
        :return: None
        :raises: Assertion error when size is not an positive integer >0
        :precondition: size must be a positive integer >0
        :complexity: best and worst case is O(n) where n is the size of the array.
        :postcondition: an array of "size = n" is created and count is set to 0
        """
        assert isinstance(size,int),"Only integer input allowed"
        assert size > 0, "Size should be positive and >0"
        self.array = size * [None]
        self.count = 0
        self.array_size = size

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
        :precondition: index provided must be positive integer in the range >0 and <count+1
        complexity: best case and worst case is O(1) as it takes constant time to access any position in the array.
        :postcondition: item is found at valid index and returned to user
        """
        assert isinstance(index, int), "Only integer input allowed"
        index = index -1
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
        :precondition: key provided must be positive integer in the range >0 and <count+1
        complexity: best case and worst case is O(1) as it takes constant time to access any position in the array.
        :postcondition: item is set at valid index given by user
        """
        assert isinstance(key, int), "Only integer input allowed"
        key = key - 1
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

        if isinstance(other,List):
            check = True
            for i in range(1,len(other)+1):
                x = other.__getitem__(i)
                y = self.__getitem__(i)
                if x!= y:
                    check = False
                    break

            return check

        elif isinstance(other,list):
            check = True
            for i in range(len(other)):
                x = other[i]
                y = self.__getitem__(i+1)
                if x!= y:
                    check = False
                    break

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

    def remove(self, item):
        """
        This function removes the first instance of the item from the list
        :param item: item to remove from the list
        :return: returns True is item is removed
        :raises: Assertion error if list is empty and ValueError if item not found
        :precondition: item provided must be in the list
        complexity: best case and worst case is O(n) where n is the number of items in the list
        :postcondition: first instance of item is removed.
        """
        assert not self.is_empty(), 'Cannot remove an item from empty list'

        found = False
        for i in range(self.count):
            if self.array[i] == item:
                found = True
                index = i
                break

        if found == False:
            raise ValueError

        for j in range(index + 1, self.count):
            self.array[j - 1] = self.array[j]

        self.count -= 1
        return True

    def delete(self, index):
        """
        This function deletes the item at the given index by the user
        :param index: position at which the item is present to delete
        :return: True is item at index is deleted
        :raises: Assertion error if index is not integer and Indexerror if index is out of range
        :precondition: valid index is provided where valid index starts from 1
        :complexity: best case is O(1) if index to be deleted is the last item and worst case is O(n) if item to be deleted is at index 0
        :postcondition: item is deleted at valid index
        """
        assert isinstance(index, int), "Only integer input allowed"
        index = index - 1
        if index < 0 or index >= self.count:
            raise IndexError

        for i in range(index, self.count - 1):
            self.array[i] = self.array[i + 1]
        self.count -= 1

        return True

    def append(self,item):
        """
        This function adds item to the end of the list
        :param item: the item to add at the end of the list
        :return: True when item is added to end of list or not
        :raises: No exceptions
        :precondition: item must be given as paramter to add to end of list
        :complexity: best case and worst case is O(n) when new array needs to be created with size 10 times the size of the previous full array
        :postcondition: item is added at end of list
        """
        has_space_left = self.is_full()
        if has_space_left == False:
            self.array[self.count] = item
            self.count += 1

        else:
            copy_array = [None]*self.array_size

            for i in range (self.array_size):
                copy_array[i] = self.array[i]

            self.array = [None] * self.array_size * 10
            self.array_size = self.array_size * 10
            self.count = 0

            for i in range(len(copy_array)):
                self.array[i] = copy_array[i]
                self.count += 1

            self.array[self.count] = item
            self.count += 1

        return True


    def insert(self,index,item):
        """
        This function places item at given index by the user and shifting other items
        :param index: position to place item before
        :param item: item to insert at position
        :return: True or False depending on if item is inserted or not
        :raises: Assertion error is raised if index is not an integer and IndexError is raised if index is out of range
        :complexity: best case is 0(1) if item is inserted at the end of the list and worst case is O(n) if item is inserted at first index
        :precondition: valid index must be entered and a item must be given as parameter and valid index starts from 1
        :postcondition: item inserted at valid index
        """
        assert isinstance(index, int), "Only integer input allowed"
        index = index - 1
        if index <0 or index> self.count:
            raise IndexError

        elif self.is_full() == False:

            if index == self.count:
                self.append(item)
                return True
            else:
                for i in range(self.count-1,index-1,-1):
                    self.array[i+1] = self.array[i]

                self.array[index] = item
                self.count+= 1
                return True

        else:
            copy_array = [None] * self.array_size

            for i in range(self.array_size):
                copy_array[i] = self.array[i]

            self.array = [None] * self.array_size * 10
            self.array_size = self.array_size * 10
            self.count = 0

            for i in range(len(copy_array)):
                self.array[i] = copy_array[i]
                self.count += 1

            if index == self.count:
                self.append(item)
                return True
            else:
                for i in range(self.count - 1, index - 1, -1):
                    self.array[i + 1] = self.array[i]

                self.array[index] = item
                self.count += 1
                return True

class Special_Command_Line:
    def __init__(self):
        """
        This function makes List object named text_editor and stack
        :param: None
        :return: None
        :raises: No exceptions
        :precondition: None
        :postcondition: None
        :complexity: best and worst case depends on the menu() and List() and Stack() class
        """
        self.text_editor = List()
        self.stack = Stack()
        self.menu()

    def menu(self):
        """
        This function is from where all the other functions are called
        :param text_editor: List ADT
        :return:None
        :raises: No exceptions
        :precondition: List array ADT must be used as input
        :complexity: best case is 0(1) if user exits and worst case is dependent until the user quits.
        :postcondition: manipulation of the list ADT is doable
        """
        valid_commands = ['insert', 'read', 'write', 'print',
                          'delete', 'frequency', 'undo', 'exit']

        while True:
            try:
                option = input('')

                option = option.strip()
                data = option.split()
                if data[0] in valid_commands:
                    break
                else:
                    print('?')
                    self.menu()

            except (IndexError):
                print('?')
                self.menu()

        if data[0] == 'insert':
            try:
                if len(data) == 2:
                    user_num = int(data[1])
                    user_line = input('')
                    save_insert_undo = user_num
                    self.text_editor.insert(user_num, user_line)
                    self.stack.push(['insert', save_insert_undo])
                    self.menu()
                else:
                    print('?')
                    self.menu()
            except (TypeError, ValueError, IndexError):
                print('?')
                self.menu()

        elif data[0] == 'read':

            if len(data) == 2:
                user_filename = data[1]
                txt_check = user_filename.split('.')
                save_read_undo = len(self.text_editor)
                if len(txt_check) == 2 and txt_check[1] == 'txt' and txt_check[0].strip() != '':
                    check = self.read_file(user_filename)
                    if check == False:
                        print('?')
                        self.menu()
                    else:
                        self.stack.push(['read', save_read_undo])
                        self.menu()
                else:
                    print('?')
                    self.menu()
            else:
                print('?')
                self.menu()

        elif data[0] == 'write':
            if len(data) == 2:
                user_filename = data[1]
                txt_check = user_filename.split('.')
                if len(txt_check) == 2 and txt_check[1] == 'txt' and txt_check[0].strip() != '':
                    check, check1 = self.Write_Filename(user_filename)
                    if check == False:
                        print('?')
                        self.menu()
                    elif check == 'Old File Re-written':
                        self.stack.push(['write', user_filename, check1])
                        self.menu()
                    elif check == 'New File Re-written':
                        self.stack.push(['write', user_filename])
                        self.menu()
                else:
                    print('?')
                    self.menu()
            else:
                print('?')
                self.menu()

        elif data[0] == 'print':
            try:
                if len(data) == 1:
                    empty = ''
                    check = self.PrintNum(empty)
                    if check == False:
                        print('?')
                        self.menu()
                    else:
                        self.menu()

                elif len(data) == 2:
                    try:
                        user_num = int(data[1])
                        check = self.PrintNum(user_num)
                        if check == False:
                            print('?')
                            self.menu()
                        else:
                            self.menu()
                    except (TypeError, ValueError):
                        print('?')
                        self.menu()
                else:
                    print('?')
                    self.menu()
            except IndexError:
                print('?')
                self.menu()

        elif data[0] == 'delete':
            if len(data) == 1:
                if self.text_editor.count == 0:
                    print('?')
                    self.menu()

                save_undo_delete = len(self.text_editor)
                self.text_editor.count = 0
                self.stack.push(['delete', save_undo_delete])
                self.menu()

            elif len(data) == 2:
                try:
                    user_num = int(data[1])
                    save_item = self.text_editor[user_num]
                    self.text_editor.delete(user_num)
                    self.stack.push(['delete', user_num, save_item])
                    self.menu()
                except (TypeError, ValueError, IndexError):
                    print('?')
                    self.menu()

        elif data[0] == 'frequency':
            if len(data) == 1:
                check = self.frequency()
                if check == False:
                    print('?')
                    self.menu()
                else:
                    self.menu()
            else:
                print('?')
                self.menu()

        elif data[0] == 'undo':
            if len(data) == 1:
                check = self.undo()
                if check == True:
                    self.menu()
                else:
                    print('?')
                    self.menu()
            else:
                print('?')
                self.menu()

        elif data[0] == 'exit':
            if len(data) == 1:
                sys.exit()
            else:
                print('?')
                self.menu()


    def read_file(self,filename):
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
        try:
            assert isinstance(filename, str), 'Filename should be a string'
        except AssertionError:
            return False

        try:
            file = open(filename, 'r')
            for line in file:
                self.text_editor.append((line.strip("\n")))

            file.close()
        except (FileNotFoundError,TypeError):
            return False

        return True


    def Write_Filename(self,filename):
        """
        This function writes line from the list into the file
        :param alist: List ADT
        :param filename: name of the file to which lines are written
        :return:True or False depending on if the file is found or not
        :raises: Assertion error if filename is not a string and FileNotFoundError if file is not found
        :precondition: list and valid filename is entered which exits
        :complexity: best and worst case is O(n) where n is the number of lines in the list
        :postcondition: All the lines of a file are written to the file line by line
        """
        try:
            assert isinstance(filename, str), 'Filename should be a string'
        except AssertionError:
            return False,None

        if  len(self.text_editor) == 0:
            return False,None

        try:
            file = open(filename, 'r')


            save_contents = []
            file = open(filename, 'r')
            for line in file:
                save_contents.append(line)

            file.close()

            file = open(filename, 'w')
            for i in range(1,self.text_editor.count+1):
                file.write("{}\n".format(self.text_editor[i]))

            file.close()
            message = 'Old File Re-written'
            return message,save_contents

        except (FileNotFoundError, TypeError):
            file = open(filename, 'w')
            for i in range(1, len(self.text_editor) + 1):
                file.write("{}\n".format(self.text_editor[i]))

            file.close()
            message2 = 'New File Re-written'
            return message2, None


    def PrintNum(self,index):
        """
        This function is used to print lines from the list
        :param alist: List ADT
        :param index: the line to print
        :return: True or False depending on if it is possible to print
        :precondition: valid index must be provided
        :complexity: best case is O(1) if only one line is needed to be printed and worst case is O(n) where n is the number of lines in the list
        :postcondition: lines are printed properly from the list
        """
        try:
            if isinstance(index, int) != True and index == '':
                if  len(self.text_editor) == 0:
                    return False
                else:
                    for i in range(1, len(self.text_editor)+1):
                        print('Line Number: ' + str(i) + '    |   ', end='                                   ')
                        print(self.text_editor[i])

                    return True


            print('Line Number: ' + str(index) + '    |   ' + '                                   ' + self.text_editor[index])
            return True
        except IndexError:
            return False


    def frequency(self):
        """
        This function is used to find to count of each word in the list
        :param alist: List ADT
        :return: True or False depending on the List
        :raises: No exceptions
        :precondition: None
        :complexity: best and worst case is O(n^2) where n is the number of lines in the list
        :postcondtion: None
        """
        if  len(self.text_editor) == 0:
            return False

        words = []
        invalid = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', ']', '[', '/', '?', ';', ':',
                   '>', '<', '', ',', '"','.']
        numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

        for line in range(1,len(self.text_editor)+1):
            Line = self.text_editor[line]
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

        List = []
        for i in range(len(words)):
            count = 1
            check = words[i]
            for j in range(i + 1, len(words)):
                if words[j] == check:
                    count += 1

            if check not in List:
                List.append(check)
                List.append(count)

        if List == []:
            return False

        format_str = '{0:30}'
        format_str1 = '{0:20}'
        for i in range(0, len(List), 2):
            print(format_str.format(List[i]), end='\t')
            print(format_str1.format(List[i+1]))

        return True


    def undo(self):
        """
        This function is used to undo actions done by the user
        :param stack: stack ADT
        :param alist: List ADT
        :return: True or False depending on if the action was undo or not
        :raises: No exceptions
        :precondition: stack ADT and List ADT must be parameters
        :complexity: depends on which type of operation is being undo
        :postcondition: appropriate action is undoed
        """
        if len(self.stack) == 0:
            return False

        previous = self.stack.pop()
        if previous[0] == 'insert':
            self.text_editor.delete(previous[1])
            return True

        if previous[0] == 'read':
            self.text_editor.count = previous[1]
            return True
        if previous[0] == 'write':
            if len(previous) == 2:
                file = open(previous[1], 'w')
                file.write('')
                return True
            elif len(previous) == 3:

                file = open(previous[1], 'w')
                for i in range(len(previous[2])):
                    file.write(previous[2][i])

                file.close()
                return True

        if previous[0] == 'delete':
            if len(previous) == 2:
                self.text_editor.count = previous[1]
                return True
            elif len(previous) == 3:

                self.text_editor.insert(previous[1],previous[2])
                return True

Special_Command_Line()

