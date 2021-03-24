def process_file(filename):
    """
        This function processes the words in the files and removes all the invalid characters.
        :param filename: name of the to process
        :return: processed string
        :raises: None
        :precondition: valid filename already in the directory
        :complexity: best and worst case is O(n^2) where n is the number of lines.
        :postcondition: processed string returned
        """

    file = open(filename, "r")
    string = ''
    for line in file:
        for character in line:
            if   (ord(character) >= 65 and ord(character) <= 90) or (ord(character) == 32): string+= character
            elif (ord(character) >= 97 and ord(character) <= 122): string+= chr(ord(character) - 32)
            else: string+= ' '
    return string

def write_to_file(filename,container):
    """
        This function writes lines to a file
        :param filename: name of the file where contents will be written to
        :param container: list of lines to write
        :return: None
        :raises: None
        :precondition: valid filename
        :complexity: best and worst case is O(n) where n is the size of the array.
        :postcondition: contents written to file
        """

    file = open(filename, 'w')
    for item in container:
        if (len(item.strip()) != 0):
            if len(item)!=1:
                file.writelines(item + '\n')
    file.close()

write_to_file('splitwords.txt',process_file("sample_input.txt").split(' '))
