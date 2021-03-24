'''
Given an array of ints, is it possible to choose a group of some of the ints, beginning at the start index, such that the group sums to the given target?
 However, with the additional constraint that all 6's must be chosen. (No loops needed.)

groupSum6(0, [5, 6, 2], 8) → true
groupSum6(0, [5, 6, 2], 9) → false
groupSum6(0, [5, 6, 2], 7) → false
'''

def sum_subsets(the_list,l,r,list1,target,e):
    global count1
    result = check(list1)
    result1 = check_six(list1,e)
    if result == target and result1==True:
        count1 += 1
        print(list1)
    else:
        for i in range(l,r+1):
            list1.append(the_list[i])
            q = sum_subsets(the_list,i+1,r,list1,target,e)
            list1.pop()



count1 = 0
def check(list1):
    total = 0
    for i in range (len(list1)):
        total = total + list1[i]

    return total

def check_six(list1,n):
    count = 0
    for i in range(len(list1)):
        if list1[i] == 6:
            count += 1

    if count==n:
        return True
    else:
        return False

def cal_six(values):
    count = 0
    for i in range(len(values)):
        if values[i]==6:
            count+= 1
    return count

values = [5,6,2,7,6]
e = (cal_six(values))
sum_subsets(values,0,len(values)-1,[],19,e)
