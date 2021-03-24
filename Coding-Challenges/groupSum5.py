'''
Given an array of ints, is it possible to choose a group of some of the ints, such that the group sums to the given target with these additional constraints: all multiples of 5 in the array must be included in the group.
If the value immediately following a multiple of 5 is 1, it must not be chosen. (No loops needed.)

groupSum5(0, [2, 5, 10, 4], 19) → true
groupSum5(0, [2, 5, 10, 4], 17) → true
groupSum5(0, [2, 5, 10, 4], 12) → false
'''

def sum_subsets(the_list,l,r,list1,target,temp):
    result = check(list1)
    result1 = check_five(list1,temp)
    if result == target and result1 ==True:
        print(list1)
    else:
        for i in range(l,r+1):
            list1.append(the_list[i])
            q = sum_subsets(the_list,i+1,r,list1,target,temp)
            list1.pop()

def check_five(list1,n):
    count = 0
    for i in range(len(list1)):
        if list1[i] % 5==0:
            count += 1

    if count==n:
        result = check_1(list1)
        if result==True:
            return True
        else:
            return False
    else:
        return False

def cal_five(values):
    count = 0
    for i in range(len(values)):
        if values[i]%5 == 0:
            count+= 1

    return count

def check_1(list1):
    for i in range(len(list1)):
        if list1[i] % 5 == 0 and (i+1 <len(list1)):
            if list1[i+1]==1:
                return False
    return True

def check(list1):
    total = 0
    for i in range (len(list1)):
        total = total + list1[i]

    return total



values = [2,5,10,4,1]
temp = cal_five(values)
sum_subsets(values,0,len(values)-1,[],20,temp)