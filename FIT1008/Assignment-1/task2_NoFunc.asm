#----------------------------------------------------------------------------------------------------------------------------------------		
#all the global variables are stored here
#----------------------------------------------------------------------------------------------------------------------------------------		
.data

prompt:		.asciiz "Enter the number of values"
prompt1:	.asciiz "Value: "
newline: 	.asciiz "\n"
size:		.word 0
the_list:	.word 0 
i:		.word 0
upper:		.word 0
lower:		.word 0
a:		.word 0
.text
#List creation starts from here
#----------------------------------------------------------------------------------------------------------------------------------------

#size = int(input('Enter the size of the list'))

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
				#list creation starts here
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
				# i acts as a counter to stop the loop
				
#i = 0

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

#    i = i + 1

	addi $t0,$t0,1		#i = i + 1
	sw $t0,i
	
	j loop

#Reading values into the list from user ends from here
#----------------------------------------------------------------------------------------------------------------------------------------
				#upper stores the address of the last word in the array the_list
				#lower stores the address of the first word in the array the_list
				

continue:

#lower = 0

	lw $s0,the_list		#the address of the first byte is loaded into $s0
	addi $s0,$s0,4
	sw $s0,lower		#the address of the first byte is stored into lower variable
	
#upper= size -1

	lw $s0,the_list
	lw $s1,size
	addi $s1,$s1,-1
	addi $s5 ,$0,4
	mul $s2,$s5,$s1
	addi $s2,$s2,4
	add $s2,$s2,$s0		#$s2 contains the address of the last byte
	sw $s2,upper		#the address of the LAST byte is stored into lower variable
	
	

list_reverse:
	
	

# while (lower <= upper):
while: 	lw $s0,upper		#store address of last byte in $s0
	
	lw $s1,lower		#store address of first byte in $s1
	blt $s0,$s1,end		#if $s0 = $s1 then the array is reversed and jump to print the array


#a = the_list[upper]	

	lw $t0,0($s0)		#save value at $s0(upper) position in $t0
	
	lw $t1,a		
	addi $t1,$t0,0
	sw $t1,a		#save value in a variable

#print(a,end=' ')	
	lw $t0,a
	
	addi $a0,$t0,0
	li $v0,1
	syscall
	
	li $a0,32
	li $v0,11
	syscall

#upper = upper - 1


	lw $s0,upper
	addi $s0,$s0,-4	
	sw $s0,upper		#reducing the upper address
	
	j while
	
	
end:
	li $v0,10		#end
	syscall	

#the program ends here
#----------------------------------------------------------------------------------------------------------------------------------------		
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@	
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@	
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#----------------------------------------------------------------------------------------------------------------------------------------		
