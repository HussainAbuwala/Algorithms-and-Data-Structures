#-------------------------------------------------------------
#-------------------------------------------------------------


user_input = 0


user_input = int(input("Please Enter a year Greater than or equal 1582: "))

while user_input <1582:

    user_input = int(input("Please Enter a year Greater than or equal 1582: "))

def is_leap_year(User_input):


    '''
    This functions implements checking if input of user is a leap year
    :param User_input: year to check for leap year
    :return: returns true is its a leap year or else returns false 
    :raise: no exceptions
    :precondition: none
    :complexity:best case 0(1), worst case 0(1)
    
    '''
    check_num = 4
    check_num1 = 100
    check_num2 = 400
    
    if (User_input % check_num) == 0 and (User_input % check_num1) != 0:
        return True
    elif (User_input % check_num2) == 0:
        return True
    else:
        return False


check = is_leap_year(user_input)

if check == True:
    print('The year you entered is a leap year :) !!')
else:
    print('The year you entered is not a leap year :( !!')

#-----------------------------------------------------------------------
#-----------------------------------------------------------------------
