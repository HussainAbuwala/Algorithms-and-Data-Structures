from LZSS_optimised_v2 import LZSS
from LZSS_optimised_v2 import decode_string
from Elias_code import ascii_to_bin
from Elias_code import elias_encode
from Elias_code import elias_decode
from Elias_code import bin_to_dec
import argparse
import sys

#NAME - HUSSAIN SADIQ ABUWALA
#STUDENT-ID - 27502333
'''
Description: encodes the given text
Algorithm used: LZSS
Param:  string to encode
Param:  W
Param:  L
return: encoded string
'''
def encode(string_to_encode,W,L):

    all_code_words = LZSS(W,L,string_to_encode)
    encode_string = ""

    for code_word in all_code_words:

        if(code_word[0] == 0):

            offset = code_word[1]
            length = code_word[2]
            encode_code_word = elias_encode(0) + elias_encode(offset) + elias_encode(length)
            encode_string = encode_string + encode_code_word

        elif(code_word[0] == 1):

            ascii_char = code_word[1]
            encode_code_word = elias_encode(1) + ascii_to_bin(ascii_char)
            encode_string = encode_string + encode_code_word


    return encode_string

def run_command_line():

    name = sys.argv[1]
    file_text = open(name, 'r')
    text = file_text.read().strip()
    file_text.close()


    W = int(sys.argv[2])
    L = int(sys.argv[3])


    final_result = encode(text,W,L)
    print("encoding finished")

    file = open('output_lzss_encoder.txt', 'w')

    file.write(final_result)
    file.close()


def run_alternate():
    name = input("Please enter File Name: ")
    file_text = open(name, 'r')
    text = file_text.read().strip()
    file_text.close()


    W = int(input("Enter W: "))
    L = int(input("Enter L: "))

    final_result = encode(text, W, L)

    file = open('output_lzss_encoder.txt', 'w')

    file.write(final_result)
    file.close()



if __name__ == '__main__':
    #run_command_line()
    run_alternate()
    #text = "life_is_a_code_either_you_crack_it_or_it_cracks_you"
    #text = "AACCCTAAACCCTAAACCCTAAACCCTAAACCCTAAACCCTAAACCTAAACCCTGAACCCTAAACCTAAACCCTGAAC"
    #text = "aacaacabcaba"
    #text = "TAATGTTACTTAATTAGTACTAAGGATTCATCTCATGTAGGTCTTATTATCATATATGGTGCACCTAGATGCATAATATCATCCAATATATCTCATTTAGTACTACTATGATGACTTATATGATCATGTTCTTACTCATTACTTCATCTACTATCGTTTTTATACCTTAATATTACTAATTCTGTCTCTTCAGGTGCACTTTGATGCACAATAATGTCAATTATTACTTATTTCTTACTACTATCTTGACTTATATGATGACTATTGTACTTCTTAGGTCAATTTTAGTGTTCATCTTATCCTTTTATTACTATTTTTATGTCCTTCATTGCACTTACGTGCACAATTATGCTCAATATTAGTCATTCATTAGTACTATTCTCACTTAGTTCATGTCTTTCTTACTTATAACTTCATCTACTATCATTATGTTACCTTACTATTACCAATTCCATGTCCAATGTTGCACTTACTTGCATAATCATGTCAATCATAAGTCCTTTTTTACTACTATCATCACTTATATCATCATTATTGTACTACTAAGGTCAATTATCACCTTCATTTTACCTAACTATTACTATTTTCATGTACTATATTGCACTTACATGCACAATAACATCCAATTTAAGTCAACTACTACTACTATTCTCACATAAGGTATCATTCTTCTACATTTAACTTCATTTACTAACATAATTCTACCTTACTATTACCAAATCCAGGTTCAATGTAGCACTTACATGCATAATTATGTCAATTTTAAGTCATCTTTTACTACTATTATCACTTATATCATCATTATTCTACTTCATAAGTGAACTATAACCTGAATCGTACCTTACTATTACTGTTTTCTTGTCCAACATAGCACTTATATGCACAATAATGTC"
    #text = "TAATGTTACTTAATTAGTACTAAGGATTCATCTCATGTAGGTCTTATTATCATATATGGTGCACCTAGATGCATAA"
    #text = "TACTATTACCAATTCCATGTCCAATGTTGCACTTACTTGCATAATCATGTCAATCAT"
    #text = "CGTACCTTACTATTACTGTTTT"
    '''text = ""

    file_text = open('reference.txt', 'r')
    text = file_text.read().strip()
    W = 600
    L = 400

    e = encode(text,W,L)
    print("encoding finished")
    d = decode(e,W,L)
    print("decoding finished")
    print(d == text)'''


