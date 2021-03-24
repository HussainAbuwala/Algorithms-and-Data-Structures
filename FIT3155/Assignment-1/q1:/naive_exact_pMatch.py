'''
        NAME: HUSSAIN SADIQ ABUWALA
        STUDENT-ID: 27502333

'''

def naive_pattern_match_rl(pat,text):

    txt_start_index = len(pat) - 1      #index in text from which right to left scanning will start
    matches = []
    while (txt_start_index < len(text)):

        temp_txt_index = txt_start_index    #temporary text index which moves during right to left scanning
        pat_current_index = len(pat) - 1    #pattern index which moves during right to left scanning

        while (pat_current_index >= 0):

            if (pat[pat_current_index] != text[temp_txt_index]):
                break

            pat_current_index -= 1
            temp_txt_index -= 1

        if (pat_current_index == -1):       #pattern fully matches with text[temp_txt_index + 1.........txt_start_index]
            #print(temp_txt_index + 1)
            matches.append(temp_txt_index + 1)

        txt_start_index += 1            #pattern is shifted by 1 place to the right

    return matches



if __name__ == '__main__':

    pass