from Linked_list_new import LinkedList
from Stack_ADT import Stack
from circular_queue import Circular_Queue

def reverse_link_list(linklist):

    if len(linklist) == 1:
        return linklist

    head_count = 0
    last_count = len(linklist)-1

    head = linklist._get_node(head_count)
    last = linklist._get_node(last_count)

    while head_count <= last_count:
        save = head.item
        head.item = last.item
        last.item = save

        head = head.next
        head_count += 1
        last_count -= 1

        last = linklist._get_node(last_count)

    return linklist
def add_one(linklist):

    front = linklist.head

    string = ''
    while front!= None:
        string = string + str(front.item)
        front = front.next

    string = str(int(string) + 1)

    count = 0
    front = link_list.head

    for i in range(len(string)):
        if front.item!= None:
            front.item = int(string[i])
        elif front.item == None:
            front.append(int(string[i]))

        front = front.next

    return linklist
def del_middle(linklist):

    middle = len(linklist)//2
    linklist.delete(middle)

    return linklist
def binary_to_dec(linklist):

    dec_val = []
    for i in range(len(linklist)-1,-1,-1):
        dec_val.append(2**i)

    front = linklist.head

    sum = 0
    for i in range(len(dec_val)):
        sum = sum + (front.item * dec_val[i])
        front = front.next

    return sum
def even_odd(linklist):

    even = []
    odd = []

    front = linklist.head

    while front!= None:
        if front.item %2 ==0:
            even.append(front.item)
        else:
            odd.append(front.item)

        front = front.next

    front = linklist.head

    for i in range(len(even)):
        front.item = even[i]
        front = front.next

    for j in range(len(odd)):
        front.item = odd[j]
        front = front.next

    return linklist
def merge_two_sorted(linklist,linklist2):

    i = 0
    j = 0

    front1 = linklist.head
    front2 = linklist2.head

    newlinklist = LinkedList()

    while i <len(linklist) and j<len(linklist2):
        if front1.item <= front2.item:
            newlinklist.append(front1.item)
            i+=1
            front1 = front1.next

        else:
            newlinklist.append(front2.item)
            j += 1
            front2 = front2.next

    while i<len(linklist):
        newlinklist.append(front1.item)
        i+= 1
        front1 = front1.next

    while j<len(linklist2):
        newlinklist.append(front2.item)
        j+= 1
        front2 = front2.next


    return reverse_link_list(newlinklist)
def compare_strings(linklist,linklist2):

    front1 = linklist.head
    front2 = linklist2.head

    string1 = ''
    string2 = ''

    while front1 != None:
        string1 = string1 + str(front1.item)
        front1 = front1.next

    while front2 != None:
        string2 = string2 + str(front2.item)
        front2 = front2.next

    if string1 == string2:
        return 0
    elif string1 > string2:
        return 1
    else:
        return -1
def duplicate_parenthesis(expression):

    stack = Stack()

    for i in range(len(expression)):

        if expression[i] == ')':

            top = stack.pop()

            if top == '(':
                return True

            while top!= '(':

                top = stack.peek()
                stack.pop()

        else:

            stack.push(expression[i])


    return False
def higher_precedence(top_stack,new):

    dict = {}
    dict['^'] = 2
    dict['*'] = 1
    dict['/'] = 1
    dict['+'] = 0
    dict['-'] = 0
    dict['('] = -1

    if dict[top_stack] >= dict[new]:
        return True
    else:
        return False
def infix_to_postfix(expression):

    expression = clean(expression)
    stack = Stack()
    queue = []
    i = 0
    while i < (len(expression)):

        try:
            value = int(expression[i])
            if value >=0 and value <=9 :

                j = i+1
                string1 = str(value)
                try:
                    while (j) < len(expression):
                        if int(expression[j]) >=0 and int(expression[j]) <=9 :
                            string1+= str(expression[j])
                        j+= 1

                    i = j
                    queue.append(string1)
                except ValueError:
                    i = j
                    queue.append(string1)


        except ValueError:

            if expression[i] == '(':
                stack.push(expression[i])

            elif stack.is_empty() == True:
                stack.push(expression[i])

            elif expression[i] == ')':

                while stack.is_empty() == False and stack.peek() != '(':
                    queue.append(stack.peek())
                    stack.pop()

                stack.pop()

            elif higher_precedence(stack.peek(),expression[i]) == True:

                while stack.is_empty() == False and higher_precedence(stack.peek(),expression[i]) == True:
                    queue.append(stack.peek())
                    stack.pop()

                stack.push(expression[i])

            else:
                stack.push(expression[i])

            i += 1


    while stack.is_empty() == False:
        queue.append(stack.peek())
        stack.pop()

    return queue
def eval_reverse_polish(expression):

    queue = infix_to_postfix(expression)
    stack = Stack()

    for i in range(len(queue)):
        try:
            val = int(queue[i])
            stack.push(val)
        except ValueError:
            x = stack.pop()
            y = stack.pop()
            if queue[i] == '+':
                result = y + x
                stack.push(result)
            elif queue[i] == '-':
                result = y - x
                stack.push(result)
            elif queue[i] == '*':
                result = y * x
                stack.push(result)
            elif queue[i] == '/':
                result = y / x
                stack.push(result)
            elif queue[i] == '^':
                result = y ** x
                stack.push(result)


    return stack.peek()
def clean(expression):
    string = ''

    for i in range(len(expression)):
        if expression[i].strip()!= '':
            string+= expression[i]

    return string
def find_valid_paranthesis(string):
    stack = Stack()

    valid = 0
    for i in range(len(string)):
        if string[i] == '(':
            stack.push(string[i])
        elif string[i] == ')' and stack.is_empty() == False:
            stack.pop()
            valid+= 2

    return valid
def find_longest_valid_paranthesis(string):

    '''
    NOT PERFECT AS QUESTION IS UNCLEAR
    :param string:
    :return:
    '''
    stack = Stack()

    max_valid = 0
    open = 0
    close = 0
    for i in range(len(string)):
        valid = 0
        if string[i] == '(':
            stack.push(string[i])
        elif string[i] == ')' and stack.is_empty() == False:
            while i<len(string) and stack.is_empty() == False and string[i] == ')':
                stack.pop()
                valid+= 2
                i+=1


            if valid > max_valid:
                max_valid = valid



    return max_valid
def partition_singly_linklist(linklist):
    fixed = linklist.head
    partition_index = link_list._get_node(len(linklist)-1)
    current = linklist.head
    for _ in range (len(linklist)-1):
        if current.item <= partition_index.item:
            fixed.item,current.item = current.item,fixed.item
            fixed = fixed.next
        current = current.next

    partition_index.item,fixed.item = fixed.item,partition_index.item
    return linklist
def sort_linklist_ofonly_0_1_2(linklist):

    zeroes = 0
    ones= 0
    twos = 0

    current = linklist.head

    while current!= None:
        if current.item == 0:
            zeroes+= 1
        elif current.item == 1:
            ones+= 1
        else:
            twos+= 1
        current = current.next

    current = linklist.head

    for i in range(len(linklist)):
        if zeroes!= 0:
            current.item = 0
            zeroes-= 1
        elif ones!= 0:
            current.item = 1
            ones-= 1
        else:
            current.item = 2
            twos-= 1
        current = current.next

    return linklist
def add_two_num_by_2_linklist(linklist1,linklist2):
    current1 = linklist1.head
    current2 = linklist2.head

    string1 = ''
    string2 = ''

    while current1!= None:
        string1+= str(current1.item)
        current1 = current1.next

    while current2!= None:
        string2+= str(current2.item)
        current2 = current2.next

    sum = str(int(string1) + int(string2))

    sumlist = LinkedList()

    for i in range(len(sum)-1,-1,-1):
        sumlist.insert(0,sum[i])

    return sumlist
def rotate_linklist_counter_clockwise(linklist,k):

    current = linklist.head
    count = 1

    while count!=k:
        current = current.next
        count+=1

    kth_plus_one_node = current.next

    save_current = current

    while save_current!= None:
        if save_current.next == None:
            save_last = save_current
            save_current = save_current.next
        else:
            save_current = save_current.next

    save_last.next = linklist.head
    current.next = None
    linklist.head = kth_plus_one_node

    return linklist



if __name__ == '__main__':
    link_list = LinkedList()
    link_list.append(10)
    link_list.append(20)
    link_list.append(30)
    link_list.append(40)
    link_list.append(50)
    link_list.append(60)
    print(eval_reverse_polish('1+1/2'))



