#----------------------------------------------------------------------------------------------------------------------------------------		
#all the global variables are stored here
#----------------------------------------------------------------------------------------------------------------------------------------

.data

prompt:		.asciiz "Enter the number of values"
prompt1:	.asciiz "Value: "
prompt2:	.asciiz "Pls enter size of list which is even "
prompt3:	.asciiz "Enter the temperature you want to find "
prompt4:	.asciiz "Temperature found"
prompt5:	.asciiz "Temperature not found"
newline: 	.asciiz "\n"
check:		.byte 	'F'
check1:		.byte	'T'
size:		.word 0
the_list:	.word 0 
i:		.word 0
j:		.word 0
user_temp:	.word 0

.text
#List creation starts from here but first the size inputted from user is validated
#----------------------------------------------------------------------------------------------------------------------------------------

#size = int(input('Enter the size of the list'))

				#'Enter the size of the list' print prompt
	li $v0,4
	la $a0,prompt
	syscall
	
				#print new line	
	li $v0,4
	la $a0,newline
	syscall

				#ask for user input and store the value in variable size
	li $v0,5
	syscall
	
	sw $v0,size		#value in $v0 is saved in size variable
	


#----------------------------------------------------------------------------------------------------------------------------------------

#the_list = [0]*size

				#list creation starts here

create_list:

	lw $t0,size		
	addi $t1,$0,4	
	mult $t1,$t0
	mflo $t2		#$t2 = 4*size to calculate array size of values the user will input
	
	add $a0,$t2,$t1		#$a0 = 4*size + 4 where addition is for storing the value of the size of list for which 1 word is additionally allocated
	li $v0,9		#syscall 9 is for allocating memory
	syscall			#$v0 = address of the first byte
	
	sw $v0,the_list		#save address of first byte in the_list
	sw $t0,0($v0)		#store length of the list at first position of the array
	
#list creation ends here
#----------------------------------------------------------------------------------------------------------------------------------------
#Reading values into the list from user starts from here
#----------------------------------------------------------------------------------------------------------------------------------------
				
#i = 0

				# i acts as a counter to stop the loop
	sw $0,i	

#while i < (size):

loop:	lw $t0,i
	lw $t1,size
	bge $t0,$t1,continue
	
#the_list[i] = int(input('Value: '))

				#print (Value: ') for showing user the message to input values
	li $v0,4
	la $a0,prompt1
	syscall
	
				#print new line	
	li $v0,4
	la $a0,newline
	syscall
	
				#ask for user input and store the value in array
	li $v0,5
	syscall
	
	lw $t2, the_list	#label-address which the label points to-address of the first byte
	
				#to access position in array, [address in the_list + 4 + i*4]
	addi $t3,$0,4
	mult $t3,$t0
	mflo $t4		#$t4=i * 4 or $t0 * $t3
	
	add $t4,$t4,$t3		#t4 = i*4 + 4
	add $t4,$t4,$t2		#$t4 = i*4 + 4 + address in the_list, $t4 points to the next location in the list
	
	sw $v0,0($t4)		#value that the user entered is stored in the empty position of the array after size of list
	
#i = i+1

	addi $t0,$t0,1		#i = i + 1
	sw $t0,i
	
	j loop

#Reading values into the list from user ends from here
#----------------------------------------------------------------------------------------------------------------------------------------

#user_temp = int(input('Enter the temperature you want to find'))

				#asking user for temperature input to find
	
continue:
	
	la $a0,prompt3		#syscall 4 for printing string
	li $v0,4
	syscall
	
#print new line	
	li $v0,4
	la $a0,newline
	syscall
	
#ask for user input and store the value in variable user_temp
	li $v0,5
	syscall
	
	sw $v0,user_temp

#----------------------------------------------------------------------------------------------------------------------------------------
#linear search begins here
#----------------------------------------------------------------------------------------------------------------------------------------	
while:

#while (j < size):

	lw $t0,size
	lw $t1,j
	
	bge $t1,$t0,final_check
	
#if the_list[j] == user_temp:

	lw $t2, the_list	#label-address which the label points to-address of the first byte
	
	lw $t0,j		#to access position in array of each temperature, [address in the_list + j*8]
	
	addi $t3,$0,4
	mult $t3,$t0
	mflo $t4		#$t4=j * 4 or $t0 * $t3
	add $t4,$t4,$t3		#t4 = j*4 + 4
	
	add $t4,$t4,$t2		#$t4 = j*4 + address in the_list, $t4 points to the next location in the list
	
	lw $t5,user_temp
	lw $t6,0($t4)
	
	bne $t5,$t6,count	#checking if users temperature matches temperature stored in array
	
#check = check1

	lb $t1,check1		#check = 'T'
	sb $t1,check

#break

	j final_check			
				#if temperature matches, it acts as a break statement

#j = j + 1
	
count:	lw $t1,j		#j=j + 1
	addi $t1,$t1,1
	sw $t1,j
	
	j while			#jump back to loop
	
#linear search ends here	
#----------------------------------------------------------------------------------------------------------------------------------------

	

	
final_check:

#if (check != check1):

	lb $t0,check
	lb $t1,check1
	beq $t0,$t1, positi	#checking to see which prompt to print
	
#print('Temperature not found')

	la $a0,prompt5		#printing temperature not found
	li $v0,4
	syscall
	
	j end
	
positi:

#else:
#print('Temperature found')

	la $a0,prompt4		#printing temperature is found
	li $v0,4
	syscall
	
	j end
	
end:
	li $v0,10		#exit
	syscall

#the program ends here
#----------------------------------------------------------------------------------------------------------------------------------------		
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@	
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@	
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#----------------------------------------------------------------------------------------------------------------------------------------	
	
	

		
	
	
	





