from LZSS_optimised_v2 import decode_string
from Elias_code import elias_decode
from Elias_code import bin_to_dec
import sys
import argparse

#NAME - HUSSAIN SADIQ ABUWALA
#STUDENT-ID - 27502333
'''
Description: decodes the given text
Param:  string to encode
Param:  W
Param:  L
return: decoded string
'''

def decode(string_to_decode,W,L):

    index = 0
    all_code_words = []
    while(index < len(string_to_decode)):

        start_bit = string_to_decode[index]

        if(start_bit == "0"):
            offset,n_index = elias_decode(string_to_decode,index + 1)
            length,index = elias_decode(string_to_decode,n_index)
            all_code_words.append((0,offset,length))

        else:
            char = chr(bin_to_dec(string_to_decode[index + 1:index + 9]))
            index = index + 9
            all_code_words.append((1,char))

    decoded_string = decode_string(all_code_words)
    return decoded_string



def run_command_line():

    name = sys.argv[1]
    file_text = open(name, 'r')
    text = file_text.read().strip()
    file_text.close()


    W = int(sys.argv[2])
    L = int(sys.argv[3])


    final_result = decode(text,W,L)

    file = open('output_lzss_decoder.txt', 'w')

    file.write(final_result)
    file.close()


def run_alternate():
    name = input("Please enter File Name: ")
    file_text = open(name, 'r')
    text = file_text.read().strip()
    file_text.close()


    W = int(input("Enter W: "))
    L = int(input("Enter L: "))

    final_result = decode(text, W, L)
    file = open('output_lzss_decoder.txt', 'w')

    file.write(final_result)
    file.close()

if __name__ == '__main__':
    #run_command_line()
    run_alternate()