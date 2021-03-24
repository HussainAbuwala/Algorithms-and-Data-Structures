#----------------------------------------------------------------------------------------------------------------------------------------		
#all the global variables are stored here
#----------------------------------------------------------------------------------------------------------------------------------------
.data

prompt:		.asciiz "Enter the size of the list"
prompt1:	.asciiz "Value:"
newline:	.asciiz "\n"
total:		.word 0
average:	.word 0
value:		.word 0
size:		.word 0
the_list:	.word 0
i:		.word 0
.text

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
	
	sw $v0,size

#----------------------------------------------------------------------------------------------------------------------------------------
				#List creation starts here

#the_list = [0]*size
	
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

##while i < (size):
	
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
				#looping through each element and adding them starts from here and average is calcualted at last
				#i acts as a counter in the loop
#i = 0
continue:
	addi $t0,$0,0
	sw $t0,i
	
##while i <size:
	
loop1:	
	lw $t0,i
	lw $t1,the_list		#$t1 = address of the_list
	lw $t2,size		#$t2 = size of the list
	

	bge $t0,$t2,cal		#branch if $t0 >= size

##value = the_list[i]

	addi $t3,$0,4		#$t3 = 4
	mult $t3,$t0
	mflo $t4		#$t4 = 4*i   ($t0)
	
	add $t4,$t4,$t3		#$t4 = 4*i + 4
	add $t4,$t4,$t1		#$t4 = 4*i + 4 + address of the_list
	
	lw $t5,0($t4)		#load the current item into $t5

	sw $t5,value		#save the current value in value variable

##total = total + value
	
	lw $t1,total		#load value of total into $t1
	lw $t5,value	


	add $t1,$t1,$t5		#total = total + value(current)
	sw $t1,total		#save new total value into total variable

#i = i+1

	lw $t0,i
	addi $t0,$t0,1
	sw $t0,i		#$t0 = $t0 + 1
	j loop1
	
				#calculation of average starts from here
				
#average = total //size
	
cal:	lw $t0,total		
	lw $t1,size
	lw $t3,average
	div $t3,$t0,$t1		#$t3 = total/size

	sw $t3,average		#$t3 = average
	
#print(average)

	lw $a0,average
	li $v0,1
	syscall
	
end:	li $v0,10		#end of the program
	syscall
#----------------------------------------------------------------------------------------------------------------------------------------
#calulation of average ends here and the program is exitted
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@	
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@	
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#----------------------------------------------------------------------------------------------------------------------------------------
	
	
	
