def JollyJumper(list_values):

    i = 0
    j = 0
    check = True
    while i< len(list_values):
        j = j + 1
        CheckIndex = checkIndex(j,list_values)
        if CheckIndex == False:
            return check

        sub = calAbs(list_values,i,j)
        check = checkVal(sub,list_values)
        if check == False:
            return check
        i = i + 1
    return check

def calAbs(list_values,i,j):
    sub = (abs(list_values[i] - list_values[j]))
    return sub


def checkVal(sub,list_values):
    lowerSub = 1
    Higher = len(list_values) - 1
    if (sub >= lowerSub) and (sub <= Higher):
        return True
    else:
        return False

def checkIndex(j,list_values):
    if j >= (len(list_values)):
        return False
    else:
        return True


list_values = [1,2,3,4,5,6]
check = JollyJumper(list_values)

if check == True:
    print ('It is a Jolly Jumper')
else:
    print('It is not a Jolly Jumper')





