def selection_sort(array):

    #find the smallest unsorted element and add it at the end of the sorted list

    #Invariance: At the start i elements is sorted
    for i in range(len(array)):
        #Invariance: At the start of each iteration, first i elements is sorted and is <= to all n-i elements
        min = find_min(array,i)
        swap(i,min,array)
    return array
    #when the program terminates, i = len(array) and all i elements are sorted. The invariance holds

    '''
    Worst case scenario: at each iteration, we need to iterate over one element less than the sorted list to find the minimum element.This is 
    repeated n times
    
    Best case scenarion: even if the list may be sorted from before, we still need to find the minimum element each time n times
    
    O(N^2) where N is the number of elements.
    '''


def find_min(array,j):

    min = j

    for i in range(j+1,len(array)):
        if array[i] < array[min]:
            min = i
    return min


def swap(i,j,array):
    array[i],array[j] = array[j],array[i]



def insertion_sort(array):

    #build sorted array in place , shifting elements out of the way if necessary to make room as you go

    #Invariance: at the start i-1 is sorted


    for i in range(1, len(array)):
        # Invariance: at the start of each iteration arr[0......i-1] is sorted but is not <= to remaining
        j = i
        temp = array[i]
        while j > 0 and temp < array[j-1]:
            array[j] = array[j - 1]
            j = j - 1
        array[j] = temp

        # Invariance: it holds

    #Invariance holds. as when i = len(array), array from 0 to i-1 is sorted. Basically the full array is sorted.

    return array

    '''
    worst case: the array is in reverse order, each time we need to shift each element  positions
    
    O(N^2)
    
    best case: if array is sorted, we just make a single pass without shifting any element.
    
    O(N)
    '''

def merge_sort(array):

    return _aux_merge_sort(array,0,len(array)-1)

    '''
    
    Worst-case-scenario: is when there are maximum number of comparisons during merging two arrays.
    Best-case-scenario: even if the array is sorted, we still need to go through all the breaking and recombining proccess
    
    We have a total of log(n) steps and at each step we do a merge of two arrays which cost O(N).
    So time complexity is O(NLOG(N))
    
    reccurence relation is:
    
    T(n) = 2T(n/2) + ɵ(n)
    
    '''

def _aux_merge_sort(array,i,j):

    if (j - i + 1) == 1:
        return [array[j]]

    left = (i + j) //2
    right = left + 1
    left_array = _aux_merge_sort(array,i,left)
    right_array = _aux_merge_sort(array,right,j)
    return merge(left_array,right_array)

def merge(l1,l2):

    #Invariance: At the start of each iteration,  A[p ... k - 1] is the
    #subarray which contains the k - p smallest elements of L and R,

    ''' for k <-- p to r
    13     do if L[i] <= R[j]
    14           then A[k] <-- L[i]
    15                i <-- i + 1
    16           else A[k] <-- R[j]
    17                j <-- j + 1
    '''

    # When the loop terminates (k = r), the invariance still holds

    new_array = []

    i = 0
    j = 0

    while i < len(l1) and j < len(l2):
        if l1[i] <= l2[j]:
            new_array.append(l1[i])
            i+=1
        else:
            new_array.append(l2[j])
            j+=1


    while i < len(l1):
        new_array.append(l1[i])
        i+=1

    while j < len(l2):
        new_array.append(l2[j])
        j+=1

    return new_array


def quick_sort(array):

    '''
        
    General Case:
    
    T (n) = T (k) + T (n − k) + αn #arrays of size k and n-k
    
    Worst Case:
    
    Now consider the case, when the pivot happened to be the least element of the array, so that wehadk=1andn−k=n−1. Insuchacase,wehave:
    T (n) = T (1) + T (n − 1) + αn
    
    Best Case:
    
    The best case of quicksort occurs when the pivot we pick happens to divide the array into two exactly equal parts, in every step.
    Thus we have k = n/2 and n − k = n/2 for the original array of size n.
    Consider, therefore, the recurrence:
    T(n) = 2T(n/2) + αn
    
    
    
    '''

    return _aux_quick_sort(array,0,len(array)-1)

def _aux_quick_sort(array,i,j):

    if i==j:

        return

    else:

        new_pivot = partition(array,i,j)
        left_pivot = new_pivot-1
        right_pivot = new_pivot+1

        if left_pivot >= i:
            _aux_quick_sort(array,i,left_pivot)
        if right_pivot <= j:
            _aux_quick_sort(array,right_pivot,j)

    return array

def partition(array,i,j):

    #Invariance: at the start of the for loop,

        # [i ..... fixed - 1] < pivot
        # [fixed .... current - 1] > pivot
        # [current .... pivot - 1] unknown



    pivot = j
    current = i
    fixed = i

    while current < pivot:
        if array[current] <= array[pivot]:
            swap(current,fixed,array)
            fixed+=1
        current+=1

    #loop terminates when current = pivot and the invariant still holds.

    swap(pivot,fixed,array)
    return fixed

def radix_sort(array):


    '''
    
If the width (number of digits) of the elements of the array to be sorted is w,
then we perform w passes over the array, leading to a time complexity of O(wN) for Radix Sort. 
If the input is bounded and w ≪ N, which can be considered a constant, then we can consider the time complexity to be O(N),
a linear time sort!

Best case : O(N) 
 
Of course, we must consider that if the array were to contain only distinct elements,
then the largest element must be at least size N, which has If the maximum magnitude of a number in the array is M,
and we are treating entries as base b numbers, then w = 1 + ⌊logb(M)⌋ passes are needed. digits.
This means that Radix Sort would still have a complexity of N log(N), or possibly even worse if in fact w ≫ log(N).

Worst case : O(NLOGN)

This shows us that Radix Sort should only perform particularly well on arrays
that contain many duplicate elements with a fixed (small) number of digits.
In practice, we can not assume that this will always be the case, but when dealing with data for which we know this to be true,
Radix Sort can be an excellent choice over traditional comparison-based sorting algorithms.
 
 
 
    '''

    number = array[0]

    #INVARIANCE: At the beginning of the for loop, the array is sorted on the last i digits.

    for i in range(len(str(number)) - 1, -1,-1):
        array = radix_pass(array,i)

    #The loop terminates when i= d (number if digits). Since the invariant holds, we have the numbers sorted on d digits.
    return array


def radix_pass(array,n):

    buckets = [[],[],[],[],[],[],[],[],[],[]]


    for i,item in enumerate(array):

        index = str(item)[n]
        a = buckets[int(index)]
        a.append(item)
        buckets[int(index)] = a

    b = []

    for item in buckets:
        b += item

    return b

def bubble_sort(array):

    '''
    
    Best case: if the array is already sorted, we are done. There will be no swaps
    O(N)
    Worst case: we need to perform n passes and a worst case of n-1 comparison.
    O(N^2)
    
    :param array: 
    :return: 
    

    
    '''

    # INVARIANCE: - At the beginning of the for loop, items n-i .. n-1 are already sorted and contain the i largest items in A.

    for i in range(len(array)):
        check = True

        for j in range(len(array) - i):
            if j + 1 < len(array):
                if array[j] > array[j+1]:
                    check = False
                    swap(j,j+1,array)
        if check == True:
            break

    #the loop terminates when i = n, at this point also the invariance holds.
    return array



if __name__ == '__main__':
    print(selection_sort([4,4,4,1,1,5,7,8,0,-1,-2,4,7,8,3,1,5,8]))
    print(insertion_sort([4,4,4,1,1,5,7,8,0,-1,-2,4,7,8,3,1,5,8]))
    print(merge_sort([4,4,4,1,1,5,7,8,0,-1,-2,4,7,8,3,1,5,8]))
    print(quick_sort([4,4,4,1,1,5,7,8,0,-1,-2,4,7,8,3,1,5,8]))
    print(bubble_sort([4,4,4,1,1,5,7,8,0,-1,-2,4,7,8,3,1,5,8]))
    print(radix_sort([43242,43122,34344,31311,41423,33444,23332,42143,22241,23143,23411,23312,]))

