import timeit
def fact(n):
    return fact_Special(n,1)

def fact_Special(n,result):
    start = timeit.default_timer()

    # do whatever you are doing that you need to time taken = (timeit.default_timer() - start)
    if n==0:
        taken = (timeit.default_timer() - start)
        print(taken)
        return result
    else:
        return fact_Special(n-1,result*n)

print(fact(3))