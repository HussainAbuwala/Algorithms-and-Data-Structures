#----------------------------------------------------------------------------------------------------------------------------------------		
.data

#all the global variables are stored in the .data section

prompt1:	.asciiz "Please Enter a year Greater than or equal 1582: "
prompt2:	.asciiz "The year you entered is a leap year :) !!"
prompt3:	.asciiz "The year you entered is not a leap year :( !!"
newline:	.asciiz "\n"
true:		.byte 'T'
false:		.byte 'F'
check:		.byte ' '
check_num:	.word 4
check_num1:	.word 100
check_num2:	.word 400
user_input:	.word 0

.text

#user_input = int(input("Please Enter a year Greater than 1582: "))

	li $v0,4
	la $a0,prompt1
	syscall
					#Print new line
	li $v0,4
	la $a0,newline
	syscall
					#ask for user input and store it in the variable user_input
	li $v0,5
	syscall
	sw $v0,user_input
	
#while user_input <1582:

   
while:	lw $t0,user_input

	bge $t0,1582,is_leap_year
	
#user_input = int(input("Please Enter a year Greater than 1582: "))

	li $v0,4
	la $a0,prompt1
	syscall
					#Print new line	
	li $v0,4
	la $a0,newline
	syscall
					#ask for user input again and store it in the variable user_input
	li $v0,5
	syscall
	sw $v0,user_input
	
					#jump to while loop again for verifying the user input again if it is valid
	j while



is_leap_year:

#if (user_input % check_num) == 0 and (user_input % check_num1) != 0:
	
	lw $s0,user_input
	
					#load check_num in $s1
	lw $s1,check_num
					#$s2 = $s0/$s1 where $s2 stores the remainder
	rem $s2,$s0,$s1
	beqz $s2,check2
	
#elif (user_input % check_num2) == 0:

check3: lw $s0,user_input
					#load check_num2 in $s1
	lw $s1,check_num2
					#$s2 = $s0/$s1 where $s2 stores the remainder
	rem $s2,$s0,$s1
	bne $s2, $0,status_F
	
#check = true
 	
	lb $t0,true
	sb $t0,check
	j status_check

#if (user_input % check_num) == 0 and (user_input % check_num1) != 0:
	
check2: lw $s0,user_input
	lw $s1,check_num1		#load check_num1 in $s1
	
	rem $s2,$s0,$s1			#$s2 = $s0/$s1 where $s2 stores the remainder
	beq  $s2,$0,check3			#(user_input % check_num1) != 0
	
#check = true
 	
	lb $t0,true
	sb $t0,check
	j status_check
	
#else:
#check = false

status_F:
	lb $t0,false
	sb $t0,check
	j status_check

					#it is checked if status which is $t0 is equal to true which is $t1
					
#if check == true:	
status_check:
	lb $t0, check
	lb $t1, true
					#if $t0 is not equal to $t1, that means status is false or $t0 is false	
	bne $t0,$t1,print_failure
	
#print('The year you entered is a leap year :) !!')

	li $v0,4
	la $a0,prompt2
	syscall
	j end 

#else:
#print('The year you entered is not a leap year :( !!')

print_failure:
	
	li $v0,4
	la $a0,prompt3
	syscall
	j end 


					#program ends
end:	li $v0,10
	syscall
	
#----------------------------------------------------------------------------------------------------------------------------------------		
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@	
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@	
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@	



	
	
		
	
	
	
