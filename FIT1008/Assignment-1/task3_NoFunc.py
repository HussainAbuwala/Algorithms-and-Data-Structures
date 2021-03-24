size = int(input('Enter the size of the list'))

the_list = [0]*size
i = 0
while i < (size):
    the_list[i] = int(input('Value: '))
    i = i+1

total = 0
average = 0
value = 0
i = 0
while i <size:
    value = the_list[i]
    total = total + value
    i = i+1

average = total //size
print(average)
