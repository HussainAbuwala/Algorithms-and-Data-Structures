'''
        NAME: HUSSAIN SADIQ ABUWALA
        STUDENT-ID: 27502333

'''

from z_box import my_z_box
'''

description:        - all positions in the text where the pattern matches the text is found out
param: pat          - pattern
param: text         - text
return:             - all positions in the text where the pattern matched

'''

def boyer_moore_final(pat,text):

    txt_start_index = len(pat) - 1  # index in text from which right to left scanning will start
    matches = []

    badCharacterArr = preProcessEBC(pat, 256)       #find bad character array - using space efficient version O(N) where N is size of alphabet. Trading off time
    goodSuffixArr = preProcessGoodSuffix(pat)       #find good suffix array
    matchedPrefixArr = preProcessMatchedPrefix(pat) #find matched prefix array

    while (txt_start_index < len(text)):

        temp_txt_index = txt_start_index  # temporary text index which moves during right to left scanning
        pat_current_index = len(pat) - 1  # pattern index which moves during right to left scanning

        default_shift_by = 1

        while (pat_current_index >= 0):

            if (pat[pat_current_index] != text[temp_txt_index]):  # mismatch occurs

                bad_character_shift = find_bad_character_shifts(text, pat_current_index, temp_txt_index,badCharacterArr)    #find bad character shifts
                good_suffix_shifts = find_good_suffix_shifts(pat,pat_current_index,goodSuffixArr,matchedPrefixArr)          #find good suffix shifts
                default_shift_by = max(bad_character_shift,good_suffix_shifts, default_shift_by)                            #take max
                break

            pat_current_index -= 1
            temp_txt_index -= 1

        if (pat_current_index == -1):  # pattern fully matches with text[temp_txt_index + 1.........txt_start_index]
            matches.append(temp_txt_index + 1)
            if(len(pat) > 1):
                default_shift_by = len(pat) - matchedPrefixArr[1]
            else:
                default_shift_by = 1

        txt_start_index = txt_start_index + default_shift_by  # pattern is shifted by 1 place to the right

    return matches


'''

description:                        - find the closest position of the bad character in the pattern which is leftmost of the mismatched character in the pattern
param: text                         - text
param: pattern_mismatch_index       - mismatch index in the pattern
param: text_mismatch_index          - mismatch index in the text
param: badCharacterArr              - bad character array
return:                             - number of shifts needed

'''

def find_bad_character_shifts(text,pattern_mismatch_index,text_mismatch_index,badCharacterArr):

    default_shift_by = 1
    bad_character = text[text_mismatch_index]                                                   # find the bad_character
    bad_character_pos_list_pat = badCharacterArr[ord(bad_character)]                            # find the position list of where this bad character occurs in pattern
    closest_pos = findClosestPos(pattern_mismatch_index,bad_character_pos_list_pat)             # find rightmost position of bad chracter which is left of pattern mismatch pos

    if (closest_pos != -1):
        default_shift_by = pattern_mismatch_index - closest_pos                                 # shift so that bad character in pattern is aligned with text bad character

    else:
        default_shift_by = pattern_mismatch_index + 1                                           # rightmost bad chracter is not found left of pattern mismatch, so shiht pattern
                                                                                                # ahead of bad character in text
    #print(default_shift_by)
    return default_shift_by


'''

description:                        - find if another substring is found using good suffix or matched prefix
param: pat                          - pattern
param: pattern_mismatch_index       - mismatch index in the pattern
param: goodSuffixArr                - good suffix array
param: matchedPrefixArr             - matched prefix array
return:                             - number of shifts needed

'''

def find_good_suffix_shifts(pat,pattern_mismatch_index,goodSuffixArr,matchedPrefixArr):

    default_shift_by = 1

    if(pattern_mismatch_index + 1 >= len(pat)):
        return default_shift_by

    else:

        if(goodSuffixArr[pattern_mismatch_index + 1] != -1):
            default_shift_by = (len(pat) - 1) - goodSuffixArr[pattern_mismatch_index + 1]
        else:
            default_shift_by = len(pat) - matchedPrefixArr[pattern_mismatch_index + 1]

    return default_shift_by



'''

description:                        - find the closest position of the bad character in the pattern which is leftmost of the mismatched character in the pattern
param: i                            - pattern mismatched index
param: badCharacterArr              - bad character array
return:                             - closest position

'''

def findClosestPos(i,badCharacterArr):

    pos = -1
    for j in range(len(badCharacterArr) - 1, -1,-1):

        if(badCharacterArr[j] < i):
            pos = badCharacterArr[j]
            break

    return pos

'''

description:                        - find the closest position of the bad character in the pattern which is leftmost of the mismatched character in the pattern
param: text                         - text
param: pattern_mismatch_index       - mismatch index in the pattern
param: text_mismatch_index          - mismatch index in the text
param: badCharacterArr              - bad character array
return:                             - number of shifts needed

'''

def preProcessEBC(pat,sizeOfAlphabet):

    badCharacterArr = [None] * sizeOfAlphabet       #initialise the size of the bad character array according to alphabet size

    for i in range(len(badCharacterArr)):           #each character in the alphabet has a list of strictly increasing positions where they occur in the pattern
        badCharacterArr[i] = []

    for index,character in enumerate(pat):
        badCharacterArr[ord(character)].append(index)

    return badCharacterArr

'''

description:    - find the good suffix array
param: pat      - pattern
return:         - good suffix array

'''

def preProcessGoodSuffix(pat):

    z_array = my_z_box(pat[::-1])[::-1]
    m = len(pat)
    good_suffix = [-1] * len(pat)

    for p in range(0,m - 1):
        j = (m - 1) - z_array[p] + 1
        if(z_array[p] != 0):
            good_suffix[j] = p

    return good_suffix

'''

description:    - find the matched prefix array
param: pat      - pattern
return:         - matched prefix array

'''
def preProcessMatchedPrefix(pat):

    z_array = my_z_box(pat)
    matched_prefix = [0] * len(pat)
    for i in range(len(z_array) - 1, -1, -1):

        if(z_array[i] + i - 1 == len(pat) - 1):

            matched_prefix[i] = z_array[i]

        elif(i + 1 < len(pat)):

            matched_prefix[i] = matched_prefix[i + 1]

    return matched_prefix



if __name__ == '__main__':
    pass
