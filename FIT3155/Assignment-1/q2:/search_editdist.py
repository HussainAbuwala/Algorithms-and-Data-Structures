'''
        NAME: HUSSAIN SADIQ ABUWALA
        STUDENT-ID: 27502333

'''
from boerMooreFinal import boyer_moore_final
from mergeSort import mergeSort
import argparse


def handle_case(text,pat):
    r = []

    for i in range(len(text)):
        if(text[i] == pat):
            r.append((i,0,""))
        else:
            r.append((i,1,""))
    return r
'''

description:            - edit distance of <=1 is calculated for a pattern and a text string.
param: pat              - pattern
param: text             - text
return:                 - all positions in the text where edit of <=1 is found

'''
def approximate_edit(pat,text):

    #################################### PATTERN IS DIVIDED INTO TWO PARTITIONS STARTS HERE #######################################
    if (len(pat) == 1):
        return sanitize_results(handle_case(text,pat))
        #return len(text)

    num_of_e_fst = len(pat) // 2
    num_of_e_snd = len(pat) - num_of_e_fst

    fst_partition = (0,num_of_e_fst - 1)            #start_index and end index of first partition
    snd_partition = (num_of_e_fst,len(pat) - 1)     #start_index and end_index of second partition

    all_partitions = [fst_partition,snd_partition]
    #################################### PATTERN IS DIVIDED INTO TWO PARTITIONS ENDS HERE  ########################################


    results = []
    ################################################# EACH PARTITION IS GIVEN AS A PATTERN TO AN EXACT PATTERN MATCHING ALGORTIHM (BOYER MOORE) ###############################
    for index,partition in enumerate(all_partitions):

        start_index = partition[0]
        end_index = partition[1]
        exact_matches = boyer_moore_final(pat[start_index:end_index+1],text)

        for matches in exact_matches:

            match_at_txt = matches

            # first partition has matched, check second partition for edit of <=1
            if (index == 0):


                start_text = match_at_txt + num_of_e_fst
                end_text = (start_text + num_of_e_snd) - 1

                # check if second partition has gone out of bounds
                if(end_text < len(text)):

                    text_substring = text[start_text: end_text + 1]
                    partition_substring = pat[snd_partition[0]:snd_partition[1] + 1]
                    check_hamming = find_if_hamming_less_eq_1(text_substring,partition_substring)

                    # find hamming of <= 1
                    if (check_hamming[1] == True):
                        results.append((match_at_txt,check_hamming[0],"hamming - at partition 2"))

                    # try insertion or deletion
                    else:

                        # insertion only possible if atleast one more character is avaliable in the text towards the right of the alignment of the second partition with the text
                        if (end_text + 1 < len(text)):

                            #try insertion
                            result_insert = check_second_partition_insert(text,pat,start_text,snd_partition[0])

                            if(result_insert == True):

                                results.append((match_at_txt, 1, "insert - at partition 2"))

                            #try deletion
                            else:

                                result_delete = check_second_partition_deletion(text,pat,start_text,snd_partition[0])
                                if (result_delete == True):

                                    results.append((match_at_txt, 1, "delete - at partition 2"))

                            #deletion


                        # when second partition is aligned at the end of the text with no more characters available after this alignment in the text. So insertion is not possible
                        # but deletion is possible
                        if (end_text + 1 == len(text)):

                            #try deletion
                            result_delete = check_second_partition_deletion(text,pat,start_text,snd_partition[0])
                            if (result_delete == True):
                                results.append((match_at_txt, 1, "delete - end - at partition 2"))


                #if second partition exceeds text (goes out of bounds)
                else:

                    exceeding_length = end_text - len(text) + 1

                    #only deletion is possible if the second partition has gone out of bounds by exactly one character
                    if(exceeding_length == 1):

                        #try deletion
                        result_delete = check_second_partition_deletion(text,pat,start_text,snd_partition[0])
                        if (result_delete == True):
                            results.append((match_at_txt, 1, "delete - exceed - at partition 2"))




            #second partition has matched check first partition
            else:

                end_text = match_at_txt - 1
                start_text = (end_text - num_of_e_fst) + 1

                #check if first partition has not gone out of bounds
                if(start_text >= 0):

                    text_substring = text[start_text:end_text + 1]
                    partition_substring = pat[fst_partition[0]:fst_partition[1] + 1]

                    #try hamming of <=1
                    check_hamming = find_if_hamming_less_eq_1(text_substring,partition_substring)

                    if (check_hamming[1] == True):
                        results.append((start_text,check_hamming[0],"hamming - at partition - 1"))

                    #try insertion or deletion
                    else:

                        # insertion only possible if atleast one more character is avaliable in the text towards the left of the alignment of the first partition with the text
                        if (start_text - 1 >= 0):

                            #try insertion
                            result_insert = check_first_partition_insert(text, pat, end_text, fst_partition[1])

                            if (result_insert == True):
                                results.append((start_text - 1, 1, "insert - at partition 1"))

                            #try deletion
                            else:
                                result_delete = check_first_partition_delete(text, pat, end_text, fst_partition[1])

                                if(result_delete == True):
                                    results.append((start_text + 1, 1, "delete - at partition 1"))


                        # when first partition is aligned at the end of the text with no more characters available after this alignment in the text. So insertion is not possible
                        # but deletion is possible
                        if (start_text - 1 == -1):
                            result_delete = check_first_partition_delete(text, pat, end_text, fst_partition[1])
                            if (result_delete == True):
                                results.append((start_text + 1, 1, "delete - at end partition 1"))
                            #deletion

                # if first partition exceeds text (goes out of bounds)
                else:
                    exceeding_length = abs(start_text) - abs(-1) + 1
                    
                    #only deletion is possible if the first partition has gone out of bounds by exactly one character
                    if (exceeding_length == 1):

                        #try deletion
                        result_delete = check_first_partition_delete(text, pat, end_text, fst_partition[1])

                        if (result_delete == True):
                            results.append((0, 1,"delete-exceed - at partition - 1"))

    ################################################# EACH PARTITION IS GIVEN AS A PATTERN TO AN EXACT PATTERN MATCHING ALGORTIHM (BOYER MOORE) ENDS HERE ###############################
    return sanitize_results(results)



'''

description:                - check if insert in first partition is possible
param: text                 - text
param: pat                  - pat
param: text_start_index     - start index in text where first partition is aligned
param: pat_start_index      - start index of first partition in pattern
return (a):                 - TRUE if insertion is possible
return (b):                 - FALSE if not possible

'''

def check_first_partition_insert(text,pat,text_start_index,pat_start_index):

    mismatch_pos_pat, mismatch_pos_txt = find_first_mismatch_first_partiton(text, pat, text_start_index,pat_start_index)

    if(mismatch_pos_pat == None and mismatch_pos_txt == None):
        return True

    txt_start = mismatch_pos_txt - 1

    while(mismatch_pos_pat >= 0):

        if (text[txt_start] != pat[mismatch_pos_pat]):
            return False

        mismatch_pos_pat -= 1
        txt_start -= 1

    return True


'''

description:                - check if deletion in first partition is possible
param: text                 - text
param: pat                  - pat
param: text_start_index     - start index in text where first partition is aligned
param: pat_start_index      - start index of first partition in pattern
return (a):                 - TRUE if deletion is possible
return (b):                 - FALSE if not possible

'''

def check_first_partition_delete(text,pat,text_start_index,pat_start_index):

    mismatch_pos_pat, mismatch_pos_txt = find_first_mismatch_first_partiton(text, pat, text_start_index,pat_start_index)

    if (mismatch_pos_pat == None and mismatch_pos_txt == None):
        return True

    pat_start = mismatch_pos_pat - 1

    while (pat_start >= 0):

        if (text[mismatch_pos_txt] != pat[pat_start]):
            return False

        pat_start -= 1
        mismatch_pos_txt -= 1

    return True


'''

description:                - check if insert in second partition is possible
param: text                 - text
param: pat                  - pat
param: text_start_index     - start index in text where second partition is aligned
param: pat_start_index      - start index of second partition in pattern
return (a):                 - TRUE if insertion is possible
return (b):                 - FALSE if not possible

'''

def check_second_partition_insert(text,pat,text_start_index,pat_start_index):

    mismatch_pos_pat, mismatch_pos_txt = find_first_mismatch_second_partition(text,pat,text_start_index,pat_start_index)

    if (mismatch_pos_pat == None and mismatch_pos_txt == None):
        return True

    txt_start = mismatch_pos_txt + 1
    while (mismatch_pos_pat < len(pat)):

        if(text[txt_start] != pat[mismatch_pos_pat]):
            return False

        mismatch_pos_pat+=1
        txt_start+=1

    return True



'''

description:                - check if deletion in second partition is possible
param: text                 - text
param: pat                  - pat
param: text_start_index     - start index in text where second partition is aligned
param: pat_start_index      - start index of second partition in pattern
return (a):                 - TRUE if deletion is possible
return (b):                 - FALSE if not possible

'''
def check_second_partition_deletion(text,pat,text_start_index,pat_start_index):

    mismatch_pos_pat, mismatch_pos_txt = find_first_mismatch_second_partition(text, pat, text_start_index, pat_start_index)

    if (mismatch_pos_pat == None and mismatch_pos_txt == None):
        return True

    pat_start = mismatch_pos_pat + 1

    while (pat_start < len(pat)):

        if (text[mismatch_pos_txt] != pat[pat_start]):
            return False

        pat_start += 1
        mismatch_pos_txt += 1

    return True



'''

description:                - find first mismatch position second partition and text
param: text                 - text
param: pat                  - pat
param: text_start_index     - start index in text where second partition is aligned
param: pat_start_index      - start index of second partition in pattern
return:                     - (mismatch_pos_pat, mismatch_pos_txt) is returned

'''

def find_first_mismatch_second_partition(text, pat, text_start_index, pat_start_index):
    t = text_start_index
    p = pat_start_index

    mismatch_pos_txt = None
    mismatch_pos_pat = None

    while (p < len(pat) and t < len(pat)):
        if (text[t] != pat[p]):
            mismatch_pos_txt = t
            mismatch_pos_pat = p
            break

        t += 1
        p += 1

    return (mismatch_pos_pat, mismatch_pos_txt)


'''

description:                - find first mismatch position in first partition and text
param: text                 - text
param: pat                  - pat
param: text_start_index     - start index in text where second partition is aligned
param: pat_start_index      - start index of second partition in pattern
return:                     - (mismatch_pos_pat, mismatch_pos_txt) is returned

'''

def find_first_mismatch_first_partiton(text, pat, text_start_index, pat_start_index):
    t = text_start_index
    p = pat_start_index

    mismatch_pos_txt = None
    mismatch_pos_pat = None

    while (p >= 0 and t >=0):

        if (text[t] != pat[p]):
            mismatch_pos_txt = t
            mismatch_pos_pat = p
            break

        t -= 1
        p -= 1

    return (mismatch_pos_pat, mismatch_pos_txt)

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
        results[i] = (item[0] + 1, item[1],item[2])

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


    final_result = approximate_edit(pat, text)
    file = open('output_editdist.txt', 'w')
    print("Total occurence found = " + str(len(final_result)))
    for item in final_result:
        file.write("{0:<16} {1:>5}".format(item[0], item[1]))
        file.write("\n")

    file.close()


def run_alternate():
    text_file_input = input("Please enter text file: ")
    pat_file_input = input("Please enter pattern file: ")

    file_text = open(text_file_input, 'r')
    file_pat = open(pat_file_input, 'r')

    text = file_text.read().strip()
    pat = file_pat.read().strip()

    final_result = approximate_edit(pat, text)
    file = open('output_editdist.txt', 'w')
    print("Total occurence found = " + str(len(final_result)))
    for item in final_result:
        file.write("{0:<16} {1:>5}".format(item[0], item[1]))
        file.write("\n")

    file.close()

def find_text_positions(final_result,text,pat):

    for i in range(len(final_result)):
        text_match_index = final_result[i][0] - 1
        print(text[text_match_index: text_match_index + len(pat)],pat,final_result[i][1],final_result[i][2])

if __name__ == '__main__':
    run_command_line()
    #run_alternate()

