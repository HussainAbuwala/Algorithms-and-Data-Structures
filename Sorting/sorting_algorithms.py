import statistics
def merge_sorted_arrays(L, R):
    i = 0
    j = 0
    answer = []
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            answer.append(L[i])
            i += 1
        else:
            answer.append(R[j])
            j += 1
    if i < len(L):
        answer.extend(L[i:])
    if j < len(R):
        answer.extend(R[j:])
    return answer


def quick_partition(the_list):
    a = []
    a.append(the_list[0])
    a.append(the_list[len(the_list)-1])
    a.append(the_list[(0+(len(the_list)-1))//2])
    partition_index = statistics.median(a)
    the_list[len(the_list)-1],the_list[the_list.index(partition_index)] = the_list[the_list.index(partition_index)],the_list[len(the_list)-1]
    fixed = 0

    for i in range (len(the_list)-1):
        if the_list[i] <= partition_index:
            the_list[fixed],the_list[i] = the_list[i],the_list[fixed]
            fixed += 1

    the_list[len(the_list)-1],the_list[fixed] = the_list[fixed],the_list[len(the_list)-1]
    return the_list

#print(quick_partition([4,3,2,1,0]))


def insertionSort(list):
        for i in range(1, len(list)):
            val = list[i]
            j = i - 1
            while (j >= 0) and (list[j] > val):
                list[j + 1] = list[j]
                j = j - 1
            list[j + 1] = val

        return list

print(insertionSort([4,3,2,1,0]))


def selectionsort(aList):
    for i in range(len(aList)):
        least = i
        for k in range(i + 1, len(aList)):
            if aList[k] < aList[least]:
                least = k

        swap(aList, least, i)

    return aList

def swap(A, x, y):
    tmp = A[x]
    A[x] = A[y]
    A[y] = tmp

print(selectionsort([4,3,2,1,0]))

