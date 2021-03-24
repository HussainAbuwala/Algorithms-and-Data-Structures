#----------------------------------------------------------------------------------------------------------------------------------------		
#all the global variables are stored here
#----------------------------------------------------------------------------------------------------------------------------------------

.data

prompt:		.asciiz "Enter the number of values"
prompt1:	.asciiz "Value: "
newline: 	.asciiz "\n"

.text
#List creation starts from here but first the size inputted from user is validated
#----------------------------------------------------------------------------------------------------------------------------------------
#'Enter the size of the list' print prompt

#def main():

main:

	li $v0,4
	la $a0,prompt
	syscall
	
				#print new line	
	li $v0,4
	la $a0,newline
	syscall
	
				#3*4 = 12 bytes local

	addi $fp,$sp,0		#store address of $fp into $sp
	addi $sp,$sp,-12	#make room for 3 local variables
	
				#initialise locals
	
	sw $0,-4($fp)		#size
	
				#ask for user input which is stored in $v0
				
#    size = int(input('Enter the size of the list'))

	li $v0,5
	syscall
	
	sw $v0,-4($fp)		#user input stored in size variable on stack
	
#----------------------------------------------------------------------------------------------------------------------------------------
#List creation starts from here
#----------------------------------------------------------------------------------------------------------------------------------------
#    the_list = [0]*size

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
				# m acts as a counter to stop the loop
				
#  m = 0
				
	sw $0,-12($fp)		#m
	
	loop:
	
#  while m < (size):

	lw $t0,-12($fp)		#load m variable into $t0	
	lw $t1,-4($fp)		#load size variable into $t1	
	bge $t0,$t1,continue1
	
				
#the_list[m] = int(input('Value: '))

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
	
	lw $t2, -8($fp)		#label-address which the label points to-address of the first byte
	
				#to access position in array, [address in the_list + 4 + m*4]
	addi $t3,$0,4
	mult $t3,$t0
	mflo $t4		#$t4=m * 4 or $t0 * $t3
	
	add $t4,$t4,$t3		#t4 = m*4 + 4
	add $t4,$t4,$t2		#$t4 = m*4 + 4 + address in the_list, $t4 points to the next location in the list
	
	sw $v0,0($t4)		#value that the user entered is stored in the empty position of the array after size of list
	
#m = m + 1

	lw $t0,-12($fp)		#load m into $t0
	addi $t0,$t0,1		#m = m + 1
	sw $t0,-12($fp)
	
	j loop

#Reading values into the list from user ends from here
#---------------------------------------------------------------------------------------------------------------------------------------	
				#push 2*4 = 8 bytes of argument onto stack for function SortByTemp
				
#SortByTemp(the_list,size)

continue1:	
	addi $sp,$sp,-8
				#arg1 = size(length of array)
	
	lw $t0,-4($fp)		#load size into arg1
	sw $t0,0($sp)
	
	lw $t0,-8($fp)		#load list into arg2
	sw $t0,4($sp)
	
	jal SortByTemp
	
	
				#remove arguments they are no longer needed, 2*4 = 8 bytes

	addi $sp,$sp,8
	
#median(the_list,size)
	
				#push 2*4 = 4 bytes arguments

	addi $sp,$sp,-8		#load sorted list argument into stack
	
				#arg1 = sorted list

	lw $t0,-8($fp)
	sw $t0,4($sp)
	
				#arg2 = size

	lw $t0,-4($fp)
	sw $t0,0($sp)
	
	jal median
	
				#remove arguments they are no longer needed, 2*4 = 8 bytes

	addi $sp,$sp,8
	
	li $v0,10
	syscall	


	
	
	
	
	
#---------------------------------------------------------------------------------------------------------------------------------------
				#SortByTemp function starts from here

#def SortByTemp(lists,length):

SortByTemp:

				#save $ra and $fp

	addi $sp,$sp,-8
	sw $ra,4($sp)
	sw $fp,0($sp)
	
	addi $fp,$sp,0		#copy $sp to $fp
	
				#allocate local variables
				#3*4 = 12 bytes

	addi $sp,$sp,-12	#making space in stack for local variables
	
	addi $t0,$0,1
	sw $t0,-4($fp)		#i
	
	addi $t0,$0,0		#j
	sw $t0,-8($fp)
	
	addi $t0,$0,0		#val
	sw $t0,-12($fp)

#while i<length:

while1:
	lw $t0,-4($fp)		#load i into $t0
	lw $t1,8($fp)		#load size(arg) into $t1
	
	bge $t0,$t1,backhome
	
#val = lists[i]

	lw $t2,12($fp)		#label-address which the label points to-address of the first byte
	
	addi $t3,$0,4		#to access position in array, [address in the_list + 4 + m*4]
	mult $t3,$t0
	mflo $t4		#$t4=i * 4 or $t0 * $t3
	
	add $t4,$t4,$t3		#t4 = i*4 + 4
	add $t4,$t4,$t2		#$t4 = i*4 + 4 + address in the_list, $t4 points to the next location in the list
	
	lw $t3,0($t4)		#load list[1] value into $t3
	sw $t3,-12($fp)		#save it in val local variable on stack
	
#j = i - 1

	lw $t3,-4($fp)		#$t3 = i
	lw $t2,-8($fp)		#t2 = j
	addi $t2,$t3,-1		#j = i -1
	sw $t2,-8($fp)		#saving j on stack
	
#while (j >= 0) and (lists[j] > val):	

while2:

	lw $t1,-12($fp)		#load val in $t1
	lw $t0,-8($fp)		#load j in $t0
	
	lw $t2,12($fp)		#label-address which the label points to-address of the first byte
	
	addi $t3,$0,4		#to access position in array, [address in the_list + 4 + j*4]
	mult $t3,$t0
	mflo $t4		#$t4=j * 4 or $t0 * $t3
	
	add $t4,$t4,$t3		#t4 = j*4 + 4
	add $t4,$t4,$t2		#$t4 = j*4 + 4 + address in the_list, $t4 points to the next location in the list
	
	lw $t5,0($t4)		#list[j]

	bge $t0,$0,check2
	j endwhile2	
	
check2:	ble $t1,$t5,continue	#check if val<=list[j]
	j endwhile2
	
	
continue:

#swap(lists,j)

				#pass 2*4 = 8 bytes argument to function swap through stack

	addi $sp,$sp,-8
	
	lw $t0,-8($fp)
	sw $t0,0($sp)		#saving argument on stack j
	
	lw $t0,12($fp)
	sw $t0,4($sp)		#saving list as argument on stack
	
	jal swap		#call function
	
				#remove arguments they are no longer needed , 2*4 = 8 bytes
	addi $sp,$sp,8
	
#j = j - 1

	lw $t0,-8($fp)
	addi $t0,$t0,-1	#j = j-1
	sw $t0,-8($fp)
	
	j while2
	
endwhile2:

#lists[j+1] = val

	lw $t0,-8($fp)		#load j
	lw $t2,12($fp)		#label-address which the label points to-address of the first byte
	
	addi $t3,$0,4		#to access position in array, [address in the_list + 4 + j*4]
	mult $t3,$t0
	mflo $t4		#$t4=j * 4 or $t0 * $t3
	
	add $t4,$t4,$t3		#t4 = j*4 + 4
	add $t4,$t4,$t2		#$t4 = j*4 + 4 + address in the_list, $t4 points to the next location in the list
	
	addi $t5,$t4,0		
	addi $t5,$t5,4		#j+4(j+1)
	
	lw $t6,-12($fp)		#load val variable in $t6
	sw $t6,0($t5)		#the_list[j+1]=val
	
#i = i+1

	lw $t6,-4($fp)		#load i
	addi $t6,$t6,1
	sw $t6,-4($fp)		#i = i + 1
	
	j while1
	
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
#SortByTemp function ends from here





#---------------------------------------------------------------------------------------------------------------------------------------
				#swap function starts here

#def swap(lists1,position):
	
swap:

				#save $ra and $fp

	addi $sp,$sp,-8
	
	sw $ra,4($sp)
	sw $fp,0($sp)
	
	addi $fp,$sp,0		#copy $sp to $fp
	
				#allocate local variables
				#1*4 = 4 bytes

	addi $sp,$sp,-4
	
				#initialise locals
	addi $t0,$0,0
	sw   $t0,-4($fp)	#save 0 in temp1 local variable on stack
	
#temp1 = lists1[position]

	lw $t0,8($fp)		#load arg position in $t0
	
	lw $t2,12($fp)		#label-address which the label points to-address of the first byte
	
	addi $t3,$0,4		#to access position in array, [address in the_list + 4 + position*4]
	mult $t3,$t0
	mflo $t4		#$t4=position * 4 or $t0 * $t3
	
	add $t4,$t4,$t3		#t4 = position*4 + 4
	add $t4,$t4,$t2		#$t4 = position*4 + 4 + address in the_list, $t4 points to the next location in the list

#lists1[position+1] = temp1

	lw $t3,0($t4)
	sw $t3,-4($fp)		#temp1 = list[position]
	
	addi $t3,$t4,0
	addi $t3,$t3,4		#[position + 4]
	
	lw $t5,-4($fp)	
	sw $t5,0($t3)		#list[position + 4] = temp1
	
				#remove local var

	addi $sp,$sp,4
	
				#restore $fp and $ra

	lw $fp,0($sp)
	lw $ra,4($sp)
	
	addi $sp,$sp,8
	
				#return to caller
	jr $ra
#---------------------------------------------------------------------------------------------------------------------------------------
#swap function ends here
#--------------------------------------------------------------------------------------------------------------------------------------

#def median(lst,Size):

median:

				#save $ra and $fp

	addi $sp,$sp,-8
	
	sw $ra,4($sp)
	sw $fp,0($sp)
	
	addi $fp,$sp,0		#copy $sp to $fp
	
				#allocate local variables
				#4*4 = 16 bytes

	addi $sp,$sp,-16

				#initialise locals

	addi $t0,$0,0		#index
	sw $t0,-4($fp)
	
	addi $t0,$0,0		#first_index
	sw $t0,-8($fp)
	
	addi $t0,$0,0		#sec_index
	sw $t0,-12($fp)
	
	addi $t0,$0,0		#result
	sw $t0,-16($fp)
	
#index = (Size - 1) // 2

	lw $t0,-4($fp)		#load index into $t0
	lw $t1,8($fp)		#load size into $t1
	li $t2,2
	
	addi $t1,$t1,-1		#size-1
	div  $t1,$t2		#size-1//2
	
	mflo $t0		#move quotient
	sw $t0,-4($fp)

#if (Size % 2 !=0):

	lw $t0,8($fp)		#load size
	li $t1,2
	
	rem $t2,$t0,$t1		#$t2 = size mod 2
	
	beq $t2,0,check_next

#print( lst[index])
	
	lw $t1,12($fp)		#$t1 = address of the_list
	lw $t0,-4($fp)		#$t2 = index

	
	addi $t3,$0,4		#$t3 = 4
	mult $t3,$t0
	mflo $t4		#$t4 = 4*i($t0)
	
	add $t4,$t4,$t3		#$t4 = 4*i + 4
	add $t4,$t4,$t1		#$t4 = 4*i + 4 + address of the_list
	
	lw $a0,0($t4)		#load the current item into the list
	addi $v0,$0,1
	syscall
	
				#remove local var

	addi $sp,$sp,16
	
				#restore $fp and $ra


	lw $fp,0($sp)
	lw $ra,4($sp)
	
	addi $sp,$sp,8
	
				#return to caller
	jr $ra
	
	
check_next:

#first_index = lst[index]

	lw $t1,12($fp)		#$t1 = address of the_list
	lw $t0,-4($fp)		#$t0 = index
	
	addi $t3,$0,4		#$t3 = 4
	mult $t3,$t0
	mflo $t4		#$t4 = 4*i($t0)
	
	add $t4,$t4,$t3		#$t4 = 4*i + 4
	add $t4,$t4,$t1		#$t4 = 4*i + 4 + address of the_list
	
	lw $t5,0($t4)
	sw $t5,-8($fp)		# first_index = lst[index]
	
	
#sec_index = lst[index + 1]

	lw $t1,12($fp)		#$t1 = address of the_list
	lw $t0,-4($fp)		#$t2 = index
	addi $t0,$t0,1
	
	addi $t3,$0,4		#$t3 = 4
	mult $t3,$t0
	mflo $t4		#$t4 = 4*i($t0)
	
	add $t4,$t4,$t3		#$t4 = 4*i + 4
	add $t4,$t4,$t1		#$t4 = 4*i + 4 + address of the_list
	
	lw $t5,0($t4)
	sw $t5,-12($fp)		# sec_index = lst[index + 1]

#result = int((first_index + sec_index)//2.0)

	lw $t0,-16($fp)		#load result into $t0
	
	lw $t1,-8($fp)		#load first_index
	lw $t2,-12($fp)		#load sec_index
	
	add $t3,$t1,$t2
	li $t6,2
	div $t4,$t3,$t6
	sw $t4,-16($fp)		#result = ((first_index + sec_index)/2.0)	
	
#print(result)

	lw $t4,-16($fp)
	addi $a0,$t4,0
	li $v0,1
	syscall
	
				#remove local var

	addi $sp,$sp,16
	
				#restore $fp and $ra


	lw $fp,0($sp)
	lw $ra,4($sp)
	
	addi $sp,$sp,8
	
				#return to caller
	jr $ra
	
	
	
	
	

	


