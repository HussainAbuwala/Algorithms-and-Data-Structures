#-------------------------------------------------------------
#-------------------------------------------------------------


user_input = 0
true = 'T'
false = 'F'
check = ''
check_num = 4
check_num1 = 100
check_num2 = 400

user_input = int(input("Please Enter a year Greater than or equal 1582: "))

while user_input <1582:

    user_input = int(input("Please Enter a year Greater than or equal 1582: "))
    
if (user_input % check_num) == 0 and (user_input % check_num1) != 0:
    check = true
elif (user_input % check_num2) == 0:
    check = true
else:
    check = false




if check == true:
    print('The year you entered is a leap year :) !!')
else:
    print('The year you entered is not a leap year :( !!')

#-----------------------------------------------------------------------
#-----------------------------------------------------------------------
