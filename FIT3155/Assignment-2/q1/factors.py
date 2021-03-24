from rabin_miller_p_test import miller_rabin_p_tst
from sieveOfEratosthenes import get_prime_factors
from sieveOfEratosthenes import create_sieve_with_minimum_prime_factors
import argparse

#NAME - HUSSAIN SADIQ ABUWALA
#STUDENT-ID - 27502333

'''
Description: finds the prime factors of  100 composite numbers <= N
Algorithm used: For finding prime numbers - using rabin miller
                For finding prime factors - using sieve of erastosthenes to pre-store the minimum prime factor
                
Param:  N
return: all composite numbers with its prime factors
'''
def find_100_largest_composite(N):
    k = 50
    start_n = N - 1
    count = 0
    composites = []
    while(count != 100):

        isPrime = miller_rabin_p_tst(start_n,k)
        if(isPrime):
            composite_number = start_n + 1
            composites.append(composite_number)
            count += 1
        start_n -= 1

    max_number = composites[0]
    pf_sieve = create_sieve_with_minimum_prime_factors(max_number)

    results = []
    for i in range(len(composites) - 1,-1,-1):
        c = composites[i]
        prime_factors = get_prime_factors(c,pf_sieve)
        results.append([c,prime_factors])
    return results



'''
Description: makes prime factors string for a composite
Param:  N
Param:  prime factors of N
return: prime factor string
'''
def make_prime_factors_string(n,prime_factors):

    count = 1
    factors_string = str(n) + " = " + " "
    for i in range(1,len(prime_factors)):

        if (prime_factors[i] == prime_factors[i - 1]):
            count += 1

        else:
            factors_string += str(prime_factors[i - 1]) + "^" + str(count) + " x "

            count = 1

    factors_string += str(prime_factors[len(prime_factors) - 1]) + "^" + str(count) + "\n"
    return factors_string



def run_command_line():

    parser = argparse.ArgumentParser()
    parser.add_argument('N',type=int)
    args = parser.parse_args()

    N = args.N
    results = find_100_largest_composite(N)

    file = open('output_factors.txt', 'w')


    for item in results:
        factors_string = make_prime_factors_string(item[0],item[1])
        file.write(factors_string)

    file.close()

if __name__ == '__main__':

    run_command_line()