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
false:		.byte 	'F'
true:		.byte	'T'

.text
#List creation starts from here but first the size inputted from user is validated
#----------------------------------------------------------------------------------------------------------------------------------------

				#'Enter the size of the list' print prompt
#def main():

main:

# size = int(input('Enter the size of the list'))

	li $v0,4
	la $a0,prompt
	syscall
	
				#print new line	
	li $v0,4
	la $a0,newline
	syscall
	
				#4*4 = 16 bytes local

	addi $fp,$sp,0		#store address of $fp into $sp
	addi $sp,$sp,-16	#make room for 4 local variables
	
				#initialise locals
	sw $0,-4($fp)		#size
	
				#ask for user input which is stored in $v0
	li $v0,5
	syscall
	
	sw $v0,-4($fp)		#user input stored in size variable on stack
	
#----------------------------------------------------------------------------------------------------------------------------------------
#List creation starts from here
#----------------------------------------------------------------------------------------------------------------------------------------

#the_list = [0]*size

	lw $t0,-4($fp)		#load size variable into $t0	
	addi $t1,$0,4	
	mult $t1,$t0
	mflo $t2		#$t2 = 4*size to calculate array size of values the user will input
	
	add $a0,$t2,$t1		#$a0 = 4*size + 4 where addition is for storing the value of the size of list for which 1 word is additionally allocated
	li $v0,9		#syscall 9 is for allocating memory
	syscall			#$v0 = address of the first byte
	
	sw $v0,-8($fp)		#save address of first byte in the_list
	sw $t0,0($v0)		#store length of the list at first position of the array
	
#list creation ends here
#----------------------------------------------------------------------------------------------------------------------------------------
#Reading values into the list from user starts from here
#----------------------------------------------------------------------------------------------------------------------------------------

#i = 0
				# i acts as a counter to stop the loop
				
	sw $0,-12($fp)		#i
	loop:

#while i < (size):

	lw $t0,-12($fp)		#load i variable into $t0	
	lw $t1,-4($fp)		#load size variable into $t1	
	bge $t0,$t1,continue1
	
	
				#print (Value: ') for showing user the message to input values
				
#the_list[i] = int(input('Value: '))

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
	
	lw $t2, -8($fp)		#label-address which the label points to-address of the first byte
	
				#to access position in array, [address in the_list + 4 + i*4]
	addi $t3,$0,4
	mult $t3,$t0
	mflo $t4		#$t4=i * 4 or $t0 * $t3
	
	add $t4,$t4,$t3		#t4 = i*4 + 4
	add $t4,$t4,$t2		#$t4 = i*4 + 4 + address in the_list, $t4 points to the next location in the list
	
	sw $v0,0($t4)		#value that the user entered is stored in the empty position of the array after size of list
	
#i = i+1

	lw $t0,-12($fp)		#load i into $t0
	addi $t0,$t0,1		#i = i + 1
	sw $t0,-12($fp)
	
	j loop

#Reading values into the list from user ends from here
#---------------------------------------------------------------------------------------------------------------------------------------
				
# user_temp = int(input('Enter the temperature you want to find'))

				#asking user for temperature input to find
	
continue1:
	
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
	
	sw $v0,-16($fp)		#save user input into temp

#---------------------------------------------------------------------------------------------------------------------------------------	

# linear_Search(user_temp,the_list,size)

				#push 3*4 = 12 bytes of argument onto stack for function Linear_Search

	
	addi $sp,$sp,-12
				#arg1 = size(length of array)
	
	lw $t0,-4($fp)		#load size into arg1
	sw $t0,0($sp)
	
	lw $t0,-8($fp)		#load list into arg2
	sw $t0,4($sp)
	
	lw $t0,-16($fp)
	sw $t0,8($sp)		#load temp into arg3
	
	
	jal linear_Search
	
				#remove arguments they are no longer needed, 3*4 = 12 bytes

	addi $sp,$sp,12
	
end:
	li $v0,10		#end
	syscall	
	
	
	
	
	
	
#---------------------------------------------------------------------------------------------------------------------------------------
				#linear_Search function starts from here
				
#def linear_Search(temp,lists,length):

linear_Search:
				#save $ra and $fp

	addi $sp,$sp,-8
	sw $ra,4($sp)
	sw $fp,0($sp)
	
	addi $fp,$sp,0		#copy $sp to $fp
	
				#allocate local variables
				#3*4 = 12 bytes
	
	addi $sp,$sp,-12	#making space in stack for local variables

#check = 'F'

	lb $t0,false
	sb $t0,-8($fp)		
	
#check1 = 'T'

	lb $t0,true
	sb $t0,-12($fp)
	
#j = 0

	addi $t0,$0,0
	sw $t0,-4($fp)		#j
	
	while:
	
#while (j < length):

	lw $t0,8($fp)		#arg(size)
	lw $t1,-4($fp)		#load j into $t1
	
	bge $t1,$t0,final_check
	
#if lists[j] == temp:

	lw $t2, 12($fp)		#label-address which the label points to-address of the first byte
	
	lw $t0,-4($fp)		#to access position in array of each temperature, [address in the_list + j*8]
	
	addi $t3,$0,4
	mult $t3,$t0
	mflo $t4		#$t4=j * 4 or $t0 * $t3
	add $t4,$t4,$t3		#t4 = j*4 + 4
	
	add $t4,$t4,$t2		#$t4 = j*4 + address in the_list, $t4 points to the next location in the list
	
	lw $t5,16($fp)
	lw $t6,0($t4)
	
	bne $t5,$t6,count
	
#check = check1

	lb $t1,-12($fp)		#check = 'T'
	sb $t1,-8($fp)
	
#break

	j final_check		#checking if users temperature matches temperature stored in array
				#if temperature matches, it acts as a break statement

# j = j + 1
	
count:	lw $t1,-4($fp)		#j=j + 1
	addi $t1,$t1,1
	sw $t1,-4($fp)
	
	j while			#jump back to loop
	
#----------------------------------------------------------------------------------------------------------------------------------------

	

	
final_check:

#if (check != check1):

	lb $t0,-8($fp)
	lb $t1,-12($fp)
	beq $t0,$t1, positi	#checking to see which prompt to print
	
#print('Temperature not found')
	
	la $a0,prompt5		#printing temperature is not found
	li $v0,4
	syscall
	
	j backhome
	
positi:

# else:
#print('Temperature found')
        
	la $a0,prompt4		#printing temperature is found
	li $v0,4
	syscall
	
	j backhome
	
backhome:

				#remove local variable
	addi $sp,$sp,12
	
				#restore $fp and $ra
	lw $fp,0($sp)
	lw $ra,4($sp)
	
	addi $sp,$sp,8
	
				#return to caller

	jr $ra	
		
#---------------------------------------------------------------------------------------------------------------------------------------
#linear_Search function ends from here

#the program ends here
#----------------------------------------------------------------------------------------------------------------------------------------		
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@	
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@	
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#----------------------------------------------------------------------------------------------------------------------------------------
	


	
	
