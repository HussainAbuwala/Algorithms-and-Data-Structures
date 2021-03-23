#NAME - HUSSAIN SADIQ ABUWALA
#STUDENT-ID - 27502333
import timeit
def LZSS(search_buffer_size,look_ahead_buffer_size,string):

    window_size = search_buffer_size + look_ahead_buffer_size
    char_pos_array = preprocess_text(string)

    look_ahead_buff_start_index = 0
    look_ahead_buff_end_index = look_ahead_buff_start_index + look_ahead_buffer_size - 1
    search_buff_end_index = look_ahead_buff_start_index - 1
    search_buff_start_index = search_buff_end_index - search_buffer_size + 1

    encode_code_words = []

    while(look_ahead_buff_start_index < len(string)):

        #print(search_buff_start_index,search_buff_end_index,look_ahead_buff_start_index,look_ahead_buff_end_index)

        code_words_list = find_longest_prefix(search_buff_start_index,
                                            search_buff_end_index,
                                            look_ahead_buff_start_index,
                                            look_ahead_buff_end_index,
                                            string,char_pos_array)

        if(len(code_words_list) == 2):
            encode_code_words.append(code_words_list[0])
            encode_code_words.append(code_words_list[1])
            length_to_discard = 2

        else:
            encode_code_words.append(code_words_list[0])
            code_word = code_words_list[0]
            if(code_word[0] == 1):
                length_to_discard = 1
            else:
                length_to_discard = code_word[2]

        pointers = update_pointers( string,
                                    look_ahead_buff_start_index,
                                    look_ahead_buff_end_index,
                                    length_to_discard,
                                    search_buffer_size)

        search_buff_start_index = pointers[0]
        search_buff_end_index = pointers[1]
        look_ahead_buff_start_index = pointers[2]
        look_ahead_buff_end_index = pointers[3]

    return encode_code_words


# s_b_s_i:  search buffer start index
# s_b_e_i:  search buffer end index
# l_b_s_i:  look-ahead buffer start index
# l_b_e_i:  look-ahead buffer end index

def update_pointers(string,l_b_s_i,l_b_e_i,length,search_buffer_size):

    #new_s_b_s_i = s_b_s_i + length
    new_l_b_s_i = l_b_s_i + length
    new_l_b_e_i = l_b_e_i + length
    new_s_b_e_i = new_l_b_s_i - 1
    new_s_b_s_i = new_s_b_e_i - search_buffer_size + 1


    if(new_s_b_s_i < 0):
        new_s_b_s_i = 0

    if(new_l_b_e_i >= len(string)):
        new_l_b_e_i = len(string) - 1

    return (new_s_b_s_i,new_s_b_e_i,new_l_b_s_i,new_l_b_e_i)


# find all character position in the text

def preprocess_text(text):

    array = [None] * 256
    for i in range(len(array)):
        array[i] = []

    for i in range(len(text)):
        character = text[i]
        array[ord(character)].append(i)
    return array




def find_longest_prefix(s_b_s_i,s_b_e_i,l_b_s_i,l_b_e_i,string,char_pos_array):

    start_point_1 = s_b_e_i #search buffer end_index
    start_point_2 = l_b_s_i

    look_ahead_buff_size = l_b_e_i - l_b_s_i + 1

    default_tuple = (0,0,string[l_b_s_i])

    if(start_point_1 < 0):
        return [(1,string[l_b_s_i])]

    char_positions = char_pos_array[ord(string[start_point_2])]
    p = binarySearch(char_positions,start_point_2)[1]


    for i in range(p - 1,-1,-1):
    #while (start_point_1 >= s_b_s_i):
        start_point_1 = char_positions[i]
        if((start_point_1 >= s_b_s_i) and (start_point_1 <= s_b_e_i)):
            offset,length,mismatch_char = find_longest_prefix_aux(start_point_1,start_point_2,string,l_b_e_i)
            if(length > default_tuple[1]):
                default_tuple = (offset,length,mismatch_char)
        elif(start_point_1 < s_b_s_i):
            break


    if(default_tuple[1] < 3):

        if(default_tuple[1] == 2):
            offset = default_tuple[0]
            first_char = string[start_point_2 - offset]
            second_char = string[start_point_2 - offset + 1]
            return [(1,first_char),(1,second_char)]

        elif(default_tuple[1] == 1):
            offset = default_tuple[0]
            char = string[start_point_2 - offset]
            return [(1,char)]
        else:
            return [(1,default_tuple[2])]
    else:
        return [(0,default_tuple[0],default_tuple[1])]




def find_longest_prefix_aux(start_point_1,start_point_2,string,l_b_e_i):

    i = start_point_1
    j = start_point_2

    #NEED TO MAKE SURE IF MATCHED STRING CAN EXCEED LOOK-AHEAD BUFFER
    while (i <= l_b_e_i and j <= l_b_e_i):

        if (string[i] != string[j]):
            offset = start_point_2 - start_point_1
            length = (i - 1) - start_point_1 + 1
            mismatch_char = string[j]
            return (offset,length,mismatch_char)

        i += 1
        j += 1

    offset = start_point_2 - start_point_1
    length = (i - 1) - start_point_1 + 1

    # THIS LOGIC NEEDS TO CHANGE IF MATCHED STRING CAN EXCEED LOOK-AHEAD-BUFFER
    #mismatch_char = ""
    if(j >= len(string)):
        mismatch_char = ""
    else:
        mismatch_char = string[j]
    return (offset, length, mismatch_char)


def decode_string(all_code_words):

    string = ""
    insert_at_index = len(string)

    for code_word in all_code_words:
        string = decode_string_aux(code_word,string,insert_at_index)
        insert_at_index = len(string)
    return string

def decode_string_aux(code_word,string,insert_at_index):


    if(code_word[0] == 1):
        string += code_word[1]
        return string

    else:

        offset = code_word[1]
        length = code_word[2]


        start_copy_index = insert_at_index - offset
        while (length != 0):
            string = string + string[start_copy_index]
            start_copy_index = start_copy_index + 1 % insert_at_index
            length -= 1

        return string


def binarySearch(alist, item):
    first = 0
    last = len(alist)-1
    found = (False,-1)

    while first<=last and found[0] == False:
        midpoint = (first + last)//2
        if alist[midpoint] == item:
            found = (True,midpoint)
        else:
            if item < alist[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1

    return found




if __name__ == '__main__':
    #text = "aacaacabcabaaac"
    #text2 = "abracadabrarray"
    #text3 = "aacaacabcaba"
    #preprocess_text("abbabcd")



    file_text = open('reference.txt', 'r')
    text3 = file_text.read().strip()


    start_time = timeit.default_timer()
    # code you want to evaluate
    search_buff_size = 50
    look_ahead_buff_size = 50
    all_code_words = LZSS(search_buff_size,look_ahead_buff_size,text3)
    elapsed = timeit.default_timer() - start_time
    print(elapsed)
    #print(all_code_words)
    #d_s = decode_string(all_code_words)

    #print(d_s,d_s == text3)
