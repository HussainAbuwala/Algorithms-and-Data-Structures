check = 'F'
check1 = 'T'

size = int(input('Enter the size of the list'))

the_list = [0]*size
i = 0
while i < (size):
    the_list[i] = int(input('Value: '))
    i = i+1

user_temp = int(input('Enter the temperature you want to find'))


j = 0
while (j < size):
    if the_list[j] == user_temp:
        check = check1
        break
    j = j + 1

if (check != check1):
    print('Temperature not found')
else:
    print('Temperature found')
