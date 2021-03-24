import csv
def new_string(string,j):
    s = ""
    for i in range(len(string)):
        if (i!= int(j)):
            s+= string[i]

    return s

def sum_of_factbase(n):
    sum = 0
    for i in range(len(n)):
        sum+= int(n[i])

    return sum

def factorial_of_number(n):
    n_copy = n
    factorial = 1

    while n_copy > 0:
        factorial = factorial * (n_copy)
        n_copy = n_copy - 1

    return factorial

def find_index(item,string):
    for i in range(len(string)):
        if string[i] == item:
            return i

def write_to_file(filename,container):

    file = open(filename, 'w')
    for item in container:
        file.writelines(item + "\n")
    file.close()


def csv_writer(n_time):
    """
    This function writes data into csv file
    :param n_time: data to write
    :return:None
    :raises: None
    :precondition: data to be written provided
    :complexity: best and worst case is O(n) where n is the number of data in the file
    :postcondition: All data write to csv
    """
    with open('question_1.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)

        for i in range(len(n_time)):
            spamwriter.writerow([n_time[i][0],n_time[i][1]])

