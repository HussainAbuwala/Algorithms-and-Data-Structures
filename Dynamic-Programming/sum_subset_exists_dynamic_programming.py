def sum_subset_exixts(arr,val):
    sum = _aux_sum_subset_ (arr,val,len(arr),{})
    if sum == 0:
        return False
    return True

def _aux_sum_subset_(arr,val,index,hashtable):

    if str(arr) in hashtable:
        return hashtable[str(arr)]
    elif len(arr) == 0:
        return 0
    elif len(arr) == 1 and arr[0] == val:
        return 1
    elif len(arr) == 1 and arr[0] != val:
        return 0
    else:
        sum = summation(arr,val)
        while index>-1 and sum!=1:
            new_arr = create(arr,index-1)
            sum = max(sum,_aux_sum_subset_(new_arr,val,len(new_arr),hashtable))
            index = index - 1

        hashtable[str(arr)] = sum
        return sum

def summation(arr,val):

    sum = 0
    for item in arr:
        sum += item

    if sum == val:
        print(arr)
        return 1
    return  0

def create(arr,index):

    new = []

    if index < 0:
        return new

    for i in range(len(arr)):
        if i!= index:
            new.append(arr[i])

    return new


print(sum_subset_exixts([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37],1000))
