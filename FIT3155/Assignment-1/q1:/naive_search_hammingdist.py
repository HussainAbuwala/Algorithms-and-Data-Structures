'''
        NAME: HUSSAIN SADIQ ABUWALA
        STUDENT-ID: 27502333

'''

from naive_exact_pMatch import naive_pattern_match_rl
from mergeSort import mergeSort
import argparse


'''

description:            - hamming of <=1 is calculated for a pattern and a text string.
param: pat              - pattern
param: text             - text
return:                 - all positions in the text where hamming of <=1 is found

'''

def handle_case(text,pat):
    r = []

    for i in range(len(text)):
        if(text[i] == pat):
            r.append((i,0,""))
        else:
            r.append((i,1,""))
    return r

def approximate_Hamming(pat,text):

    if (len(pat) == 1):
        return sanitize_results(handle_case(text,pat))

    num_of_e_fst = len(pat) // 2                    #number of elements in first partition
    num_of_e_snd = len(pat) - num_of_e_fst          #number of elements in second partition

    fst_partition = (0,num_of_e_fst - 1)            #start_index and end index of first partition
    snd_partition = (num_of_e_fst,len(pat) - 1)     #start_index and end_index of second partition

    all_partitions = [fst_partition,snd_partition]
    results = []

    for index,partition in enumerate(all_partitions):

        start_index = partition[0]
        end_index = partition[1]
        exact_matches = naive_pattern_match_rl(pat[start_index:end_index+1],text)

        for matches in exact_matches:

            match_at_txt = matches          #start index in txt where a partition has exactly matched

            if (index == 0):                #first partition has matched, check second partition

                #first partition has matched, check second partition

                start_text = match_at_txt + num_of_e_fst
                end_text = (start_text + num_of_e_snd) - 1

                if(end_text < len(text)):

                    text_substring = text[start_text: end_text + 1]
                    partition_substring = pat[snd_partition[0]:snd_partition[1] + 1]

                    check_hamming = find_if_hamming_less_eq_1(text_substring,partition_substring)

                    if (check_hamming[1] == True):
                        results.append((match_at_txt,check_hamming[0]))

            else:

                #check first partition
                end_text = match_at_txt - 1
                start_text = (end_text - num_of_e_fst) + 1

                if(start_text >= 0):   #first partition is not gone over left side of txt

                    text_substring = text[start_text:end_text + 1]
                    partition_substring = pat[fst_partition[0]:fst_partition[1] + 1]
                    check_hamming = find_if_hamming_less_eq_1(text_substring,partition_substring)

                    if (check_hamming[1] == True):
                        results.append((start_text,check_hamming[0]))

    return sanitize_results(results)


'''

description:            - results are sorted and duplicate are removed from the list
param: results          - list of positions in text where hamming of <=1 happened for a pattern
return:                 - sorted list of positions without duplicates

'''


def sanitize_results(results):
    if (results == []):
        return []

    for i in range(len(results)):
        item = results[i]
        results[i] = (item[0] + 1, item[1])

    mergeSort(results)

    unique_list = removeDup(results)

    return unique_list


'''

description:            - duplicates are removed from the sorted list
param: sorted_list      - list of positions in text where hamming of <=1 happened for a pattern which are sorted
return:                 - sorted list of positions without duplicates

'''

def removeDup(sorted_list):

    unique = []
    last_elem_index = len(sorted_list) - 1

    for i in range(len(sorted_list)):
        if(i + 1 < len(sorted_list)):
            if(sorted_list[i][0] != sorted_list[i + 1][0]):
                unique.append(sorted_list[i])

    unique.append(sorted_list[last_elem_index])
    return unique


'''

description:            - hamming of <=1 ia calculated between two texts
param: results          - list of positions in text where hamming of <=1 happened for a pattern
return:                 - sorted list of positions without duplicates

'''
def find_if_hamming_less_eq_1(txt1,txt2):

    mismatch = 0
    for i in range(len(txt1)):

        if(txt1[i] != txt2[i]):
            mismatch+=1
        if(mismatch > 1):
            return (None,False)

    if (mismatch == 1):
        return (1,True)
    if (mismatch == 0):
        return (0,True)


def run_command_line():

    parser = argparse.ArgumentParser()
    parser.add_argument('textFile',type=argparse.FileType('r'))
    parser.add_argument('patFile',type=argparse.FileType('r'))
    args = parser.parse_args()

    text = ""

    for line in args.textFile.read():
        text+= line.strip()

    pat = ""

    for line in args.patFile.read():
        pat+= line.strip()


    final_result = approximate_Hamming(pat, text)
    file = open('output_hammingdist.txt', 'w')
    print("Total occurence found = " + str(len(final_result)))
    for item in final_result:
        file.write("{0:<16} {1:>5}".format(item[0], item[1]))
        file.write("\n")

    print(len(final_result))

    file.close()


def run_alternate():

    text_file_input = input("Please enter text file: ")
    pat_file_input = input("Please enter pattern file: ")

    file_text = open(text_file_input,'r')
    file_pat = open(pat_file_input,'r')

    text = file_text.read().strip()
    pat = file_pat.read().strip()

    final_result = approximate_Hamming(pat, text)
    file = open('output_hammingdist.txt', 'w')
    print("Total occurence found = " + str(len(final_result)))
    for item in final_result:
        file.write("{0:<16} {1:>5}".format(item[0], item[1]))
        file.write("\n")

    file.close()


def find_text_positions(final_result,text,pat):

    for i in range(len(final_result)):
        text_match_index = final_result[i][0] - 1
        print(text[text_match_index: text_match_index + len(pat)],pat,final_result[i][1])



if __name__ == '__main__':

    run_command_line()
    #run_alternate()




