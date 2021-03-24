'''

Given an array of ints, is it possible to choose a group of some of the ints, such that the group sums to the given target with this additional constraint:
 If a value in the array is chosen to be in the group, the value immediately following it in the array must not be chosen. (No loops needed.)

groupNoAdj(0, [2, 5, 10, 4], 12) → true
groupNoAdj(0, [2, 5, 10, 4], 14) → false
groupNoAdj(0, [2, 5, 10, 4], 7) → false
'''

def sum_subsets(the_list,l,r,list1,target):
    result = check(list1)
    result1 = checkAdj(list1,the_list)
    if result == target and result1==True:
        print(list1)
    else:
        for i in range(l,r+1):
            list1.append(the_list[i])
            q = sum_subsets(the_list,i+1,r,list1,target)
            list1.pop()

def check(list1):
    total = 0
    for i in range (len(list1)):
        total = total + list1[i]

    return total

def checkAdj(list1,the_list):
    for i in range(len(list1)):
        for j in range(len(the_list)):
            if (the_list[j] == list1[i]) and ((i+1 <len(list1)) and (j+1 <len(the_list))):
                if list1[i+1]==the_list[j+1]:
                    return False

    return True





values = [1,2,3,4,5,6,8,9,10,11,12]
sum_subsets(values,0,len(values)-1,[],30,)