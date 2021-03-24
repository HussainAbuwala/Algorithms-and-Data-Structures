def permute(a, l, r):
    if l == r:
        print(a)
        print('This is final result')
        return None
    else:
        for i in range(l, r + 1):
            print('i= ' + str(i) + ',' + 'l= ' + str(l) + ',' + 'r = ' + str(r) + ',' + 'r+1 = ' + str(r+1))
            a[l], a[i] = a[i], a[l]
            print(a)
            print('This is fixing alphabets')
            result =  permute(a, l + 1, r)
            a[l], a[i] = a[i], a[l]  # backtrack
            print(a)
            print('This is the list after tracking back')


# Driver program to test the above function
string = "ABC"
n = len(string)
a = list(string)
permute(a, 0, n - 1)
