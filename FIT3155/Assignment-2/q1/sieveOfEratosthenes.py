import math
#NAME - HUSSAIN SADIQ ABUWALA
#STUDENT-ID - 27502333
def create_sieve_with_minimum_prime_factors(number):

    sieve = [-1] * (number + 1)
    start_number = 2
    while(start_number <= math.sqrt(number)):
        if(sieve[start_number] == -1):
            update_multiples(sieve,start_number,number)

        start_number += 1

    return sieve



def update_multiples(sieve,start_number,n):

    s = start_number * 2
    for multiple in range(s,n + 1,start_number):
        if(sieve[multiple] == -1):
            sieve[multiple] = start_number


def find_prime_factors(n,smallest_prime_factor_arr):

    all_prime_factors = []

    number = n
    while (number != 1):
        if(smallest_prime_factor_arr[number] == -1):
            all_prime_factors.append(number)
            break
        else:
            all_prime_factors.append(smallest_prime_factor_arr[number])
            number = number // smallest_prime_factor_arr[number]

    return all_prime_factors

def get_prime_factors(n,pf_sieve):

    min_prime_factor_arr = pf_sieve
    prime_factors = find_prime_factors(n,min_prime_factor_arr)
    return prime_factors


'''
def print_prime_factors(n,prime_factors):

    count = 1
    print(str(n) + " = ",end="  ")
    for i in range(1,len(prime_factors)):

        if (prime_factors[i] == prime_factors[i - 1]):
            count += 1

        else:
            print(str(prime_factors[i - 1]) + "^" + str(count), end=" x ")
            count = 1

    print(str(prime_factors[len(prime_factors) - 1]) + "^" + str(count))
'''

if __name__=='__main__':
    #main(522)
    pass

