from random import *
import math

#NAME - HUSSAIN SADIQ ABUWALA
#STUDENT-ID - 27502333

'''
Input: n > 2, is the number being tested for primality
input: k, a parameter that determines accuracy of the test
'''

def miller_rabin_p_tst(n,k):

    if(n == 2 or n == 3):
        return True
    if(is_even(n)):
        return False

    #factor n-1 as 2^s * t, where t is odd

    s = 0
    r = n - 1

    while (is_even(r)):
        s = s + 1
        r //= 2


    for _ in range(k):
        a = randrange(2, n - 1)
        x = pow(a, r, n)
        if x != 1 and x != n - 1:
            j = 1
            x = check_fermats_observation(j,s,x,n)
            if x != n - 1:
                return False
    return True



def check_fermats_observation(j,s,x,n):

    while j < s and x != n - 1:
        x = pow(x, 2, n)
        if x == 1:
            return False
        j += 1
    return x




def is_even(n):
    return n % 2 == 0

'''
def primeFactors(n):
    # Print the number of two's that divide n

    pf = []
    while n % 2 == 0:

        pf.append(2)
        n = n / 2

    # n must be odd at this point
    # so a skip of 2 ( i = i + 2) can be used
    for i in range(3, int(math.sqrt(n)) + 1, 2):

        # while i divides n , print i ad divide n
        while n % i == 0:
            pf.append(i)
            n = n / i

            # Condition if n is a prime
    # number greater than 2
    if n > 2:
        pf.append(n)

        # Driver Program to test above function
    return pf
'''
if __name__ == '__main__':

    print(miller_rabin_p_tst(11,222))
    n = 315



