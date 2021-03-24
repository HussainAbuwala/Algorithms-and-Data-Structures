class QuadraticProbeTable:

    def __init__(self,size=7919):
        self.count = 0
        self.array = [None] * size
        self.table_size = size
        self.collisions = 0
        self.max = 0

    def __len__(self):
        return self.count

    def hash(self,key):
        value = 0
        a = 31415
        b = 250726
        for i in range(len(key)):
            value = (ord(key[i]) + a*value ) % self.table_size
            a = a * b %(self.table_size-1)
        return value

    def __setitem__(self, key, value):
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
        position = self.hash(key)
        save = position

        for i in range(self.table_size-1):
            if self.array[position] == None:
                raise KeyError('KEY NOT FOUND')
            elif self.array[position][0] == key:
                common_cal = self.max / 100
                uncommon_cal = self.max / 1000

                if self.array[position][1] >= common_cal:
                    return 'C'

                elif self.array[position][1] >= uncommon_cal:
                    return 'UC'

                else:
                    return 'R'


            else:
                position = ((save + ((i+1) ** 2)) % self.table_size)

        raise KeyError('KEY NOT FOUND')

    def __contains__(self, key):
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
    file = open(filename, 'r')

    for line in file:
        line = line.strip('\n')
        templist.append(line)


    file.close()

    return templist

def read_words_into_dictionary(dict,filename):

    words = frequency(filename)
    for item in words:

        dict[item] = 1

    return dict

def find_rank(filename):
    dict = QuadraticProbeTable(402221)
    read_words_into_dictionary(dict, filename)
    while True:
        try:
            user_input = input('WORD: ')

            rank = dict[user_input]

            if rank == 'C':
                print('The word ' + '"' + str(user_input) + '"' + ' is ' + 'COMMON !')
            elif rank == 'UC':
                print('The word ' + '"' + str(user_input) + '"' + ' is ' + 'UNCOMMON !')
            else:
                print('The word ' + '"' + str(user_input) + '"' + ' is ' + 'RARE !')




        except KeyError:
            print('?')


if __name__ == '__main__':
    find_rank('gutenberg.txt')
