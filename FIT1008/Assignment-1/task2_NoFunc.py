upper = 0
lower = 0

size = int(input('Enter the size of the list'))

the_list = [0]*size
i = 0

while i < (size):
    the_list[i] = int(input('Value: '))
    i = i + 1
    
lower = 0
upper= size -1
    
while (upper >= lower):

    a = the_list[upper]
    print(a,end=' ')
    upper = upper - 1
