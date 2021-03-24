def min_steps_to_one(n):
    return min_steps_to_one_aux_(n,{})

def min_steps_to_one_aux_(n,hashtable):
    if  (str(n)) in hashtable:
        return hashtable[str(n)]
    elif n == 1:
        return 0
    else:
        result =  1 + min_steps_to_one_aux_(n-1,hashtable)
        if n % 2 == 0:
            result = min(result,1 + min_steps_to_one_aux_(n/2,hashtable))
        if n % 3 == 0:
            result = min(result,1 + min_steps_to_one_aux_(n/3,hashtable))

        hashtable[str(n)] = result
        return result


print(min_steps_to_one(5000))