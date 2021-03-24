#----------------------------------------------------------------------------------------------------------------------------------------		
#all the global variables are stored here
#----------------------------------------------------------------------------------------------------------------------------------------
.data

prompt:		.asciiz "Enter the size of the list"
prompt1:	.asciiz "Value:"
newline:	.asciiz "\n"

.text

#main function starts from here
main:

##def main():

#List creation starts from here
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
#----------------------------------------------------------------------------------------------------------------------------------------
	addi $fp,$sp,0		#store address of $sp into $fp
	addi $sp,$sp,-4
	
	sw $v0,-4($fp)		#local variable size is stored on the stack
#----------------------------------------------------------------------------------------------------------------------------------------
				#list creation starts here

#    the_list = [0]*size

	
	lw $t0,-4($fp)		#local variable size is loaded from stack
	addi $t1,$0,4	
	mult $t1,$t0
	mflo $t2		#$t2 = 4*size to calculate array size of values the user will input
	
	add $a0,$t2,$t1		#$a0 = 4*size + 4 where addition is for storing the value of the size of list for which 1 word is additionally allocated
	li $v0,9		#syscall 9 is for allocating memory
	syscall			#$v0 = address of the first byte
	
	addi $sp,$sp,-4
	
	sw $v0,-8($fp)		#local variable the_list is stored on the stack
	
	sw $t0,0($v0)		#store length of the list at first position of the array
	
#list creation ends here
#----------------------------------------------------------------------------------------------------------------------------------------
#Reading values into the list from user starts from here
#----------------------------------------------------------------------------------------------------------------------------------------
				# i acts as a counter to stop the loop

#i = 0

	addi $t0,$0,0
	addi $sp,$sp,-4
	sw $t0,-12($fp)		#i = 0

#while i < (size):

	loop:	
	lw $t0,-12($fp)
	lw $t1,-4($fp)		#local variable size is loaded from stack
	bge $t0,$t1,continue
	
# the_list[i] = int(input('Value: '))

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
	
				#to access position in array, [address in the_list + 4 + i*4]
	addi $t3,$0,4
	mult $t3,$t0
	mflo $t4		#$t4=i * 4 or $t0 * $t3
	
	add $t4,$t4,$t3		#t4 = i*4 + 4
	add $t4,$t4,$t2		#$t4 = i*4 + 4 + address in the_list, $t4 points to the next location in the list
	
	sw $v0,0($t4)		#value that the user entered is stored in the empty position of the array after size of list
	
#        i = i+1

	lw $t0,-12($fp)		#load i from stack
	addi $t0,$t0,1		#i = i + 1
	sw $t0,-12($fp)
	
	j loop

#Reading values into the list from user ends from here
#----------------------------------------------------------------------------------------------------------------------------------------
	continue:
	
#average = cal_aver(the_list,size)

				#saving local variables and calling the cal_aver function starts from here
				#1*4 bytes local
	
	addi $sp,$sp,-4
	
				#initialise locals
	sw $0,-16($fp)		#average
	
	addi $sp,$sp,-8		#making space for arguments to be pushed onto the stack
	lw $t0,-4($fp)		#loading size contents to be pushed as argument
	sw $t0,4($sp)		#saving it on stack
	
	lw $t0,-8($fp)		#load list address to push as argument
	sw $t0,0($sp)		#save on stack
	
	jal cal_aver		#no need to push arguments as size is global variable
	
	addi $sp,$sp,8		#removing arguments which are no longer needed
	
	sw $v0,-16($fp)		#save return value into average variable
	
# print(average)

	lw $a0,-16($fp)
	li $v0,1
	syscall
	
	li $v0,10		#exit
	syscall
	
	
#cal_aver function starts from here
#----------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------
cal_aver:

#def cal_aver(lists,length):

				#save $ra and $fp

	addi $sp,$sp,-8
	sw $ra,4($sp)
	sw $fp,0($sp)
	
	addi $fp,$sp,0		#copy $sp to $fp
	
				#allocate local variables
				#2* 4 = 8bytes
	
	addi $sp,$sp,-16
	
				#initialise locals

#total = 0

	addi $t0,$0,0		#total
	sw $t0,-4($fp)

#value = 0
	
	addi $t0,$0,0
	sw $t0,-8($fp)		#value

#final = 0

	addi $t0,$0,0
	sw $t0,-12($fp)		#final
	
#j = 0

	addi $t0,$0,0
	sw $t0,-16($fp)		#j=0 on stack
	
#while j< (length):

	lw $t0,-16($fp)		#load j into $t0
	
	loop1:
	
	lw $t1,8($fp)		#$t1 = address of the_list
	lw $t2,12($fp)		#$t2 = size of the list from stack
	lw $t0,-16($fp)
	bge $t0,$t2,cal		#branch if j >= size
	
#value = lists[j]

	addi $t3,$0,4		#$t3 = 4
	mult $t3,$t0
	mflo $t4		#$t4 = 4*($t0)
	
	add $t4,$t4,$t3		#$t4 = 4*i + 4
	add $t4,$t4,$t1		#$t4 = 4*i + 4 + address of the_list
	
	lw $t5,0($t4)		#load the current item into $t5
	sw $t5,-8($fp)		#save the current value in value variable which is local and into the stack
	
#   total = total + value

	lw $t1,-4($fp)		#load value of total from stack into $t1
	lw $t5,-8($fp)		#load the contents of value variable into $t5
	
	add $t1,$t1,$t5		#total = total + value
	sw $t1,-4($fp)		#save value into total variable in the stack
	
# j = j+1

	lw $t0,-16($fp)
	addi $t0,$t0,1
	sw $t0,-16($fp)		#j = j+1
	
	j loop1
	
	cal:
	
# final = total //length

				#calculation of average starts from here

	lw $t0, -4($fp)		#load total from stack into $t0
	lw $t1, 12($fp)		#load size into $t1
	lw $t2, -12($fp)	#load final from stack into $t2
	
	div $t0,$t1		#value of integer division stored in $t2
	mflo $t2
	sw $t2, -12($fp)	#save value of $t2 into final local variable
	
# return final

	lw $v0,-12($fp)		#return value stored in $v0
	
	addi $sp,$sp,16		#remove local variable
	
				#restore $fp and $ra

	lw $fp,0($sp)
	lw $ra,4($sp)
	addi $sp,$sp,8
	
				#return to caller
	jr $ra

#----------------------------------------------------------------------------------------------------------------------------------------
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@	
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@	
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#----------------------------------------------------------------------------------------------------------------------------------------		
	
	
	
	
