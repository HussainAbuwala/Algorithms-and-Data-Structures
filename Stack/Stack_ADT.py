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




def check_parenthesis(string):
    mystack = Stack()

    for i in range(len(string)):
        if string[i] == '(' or string[i] == '[':
            mystack.push(string[i])
        elif string[i] == ')' or string[i] == ']':
            if not mystack.is_empty():
                item = mystack.pop()
                if (item == '(' and string[i] == ']') or (item == '[' and string[i] == ')'):
                    return False

    if not mystack.is_empty():
        return False
    return True



print(check_parenthesis("([)]"))