#NAME - HUSSAIN SADIQ ABUWALA
#STUDENT-ID - 27502333
def elias_encode(N):

    code_words = [dec_to_bin(N)]

    length_of_component = len(code_words[0])  - 1
    length_component = dec_to_bin(length_of_component)

    while (length_of_component >= 1):

        code_words.append('0' + length_component[1:])
        length_of_component = len(code_words[len(code_words) - 1]) - 1
        length_component = dec_to_bin(length_of_component)

    return "".join(code_words[::-1])

def elias_decode(codeword,start):

    readlen = 1
    pos = start
    component = codeword[pos:pos + readlen]

    while (True):

        if(component[0] == '1'):
            N = bin_to_dec(component)
            return (N,pos + readlen)
        else:
            s = list(component)
            s[0] = "1"
            new = "".join(s)
            pos = pos + readlen
            readlen = bin_to_dec(new) + 1

        component = codeword[pos:pos + readlen]




def dec_to_bin(decimal_num):
    return bin(decimal_num)[2:]

def bin_to_dec(binary_num):
    return int(binary_num,2)

def ascii_to_bin(character):

    bitstring = dec_to_bin(ord(character))

    while (len(bitstring) != 8):
        bitstring = "0" + bitstring

    return bitstring

if __name__ == '__main__':

    encoded_string = elias_encode(542)
    print(encoded_string)
    print(elias_decode("012" + encoded_string,3))
    #print(ascii_to_bin("a"))
