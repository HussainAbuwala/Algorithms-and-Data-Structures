def super_mario_stairs(height):
    h = height
    for i in range(2,height+2):
        print(' '* h + '#' *i)
        h = h-1

def super_mario_half_pyramid_reflect_yaxis(height):
    h = height
    for i in range(2,height+2):
        print(' '* h + '#' *i + ' ' + '#'*i)
        h = h-1

def super_mario_half_pyramid_inverted_reflect_yaxis(height):
    h = 1
    for i in range(height+1,1,-1):
        print(' ' * h + '#' * i + ' ' + '#' *i)
        h = h + 1

def super_mario_half_pyramid_reflect_xaxis(height):
    h = height
    for i in range(2, height + 2):
        print(' ' * h + '#' * i)
        h = h - 1

    print()

    h = 1
    for i in range(height + 1, 1, -1):
        print(' ' * h + '#' * i )
        h = h + 1

def super_mario_half_pyramid_inverted_reflect_xaxis(height):
    h = 1
    for i in range(height + 1, 1, -1):
        print(' ' * h + '#' * i)
        h = h + 1

    print()

    h = height
    for i in range(2, height + 2):
        print(' ' * h + '#' * i)
        h = h - 1


def super_mario_create_sandglass(height):
    h = 1
    for i in range(height + 1, 1, -1):
        print(' ' * h + '#' * i + ' ' + '#' * i)
        h = h + 1

    h = height
    for i in range(2, height + 2):
        print(' ' * h + '#' * i + ' ' + '#' * i)
        h = h - 1

def super_mario_create_diamond(height):
    h = height
    for i in range(2, height + 2):
        print(' ' * h + '#' * i + ' ' + '#' * i)
        h = h - 1

    h = 1
    for i in range(height + 1, 1, -1):
        print(' ' * h + '#' * i + ' ' + '#' * i)
        h = h + 1

def super_mario_petronas_tower(height):
    h = height
    x = (2*height)-2

    for i in range(2, height + 2):
        for j in range(15):
            print(' ' * h + '#' * i + ' ' + '#' * i,end=' ')
            print(' ' * x + '#' * i +  ' ' + '#' * i, )
        print(end = '')
        h = h - 1
        x = x -2

def super_mario_shriti_shodh(height):
    h = (height*2)
    for i in range(4, height + 2,7):

        print(' ' * (h-7)  + '#' * i)

        h = h - 7







#super_mario_stairs(8)
#super_mario_half_pyramid_reflect_yaxis(20)
#super_mario_half_pyramid_inverted_reflect_yaxis(8)
#super_mario_half_pyramid_reflect_xaxis(8)
#super_mario_half_pyramid_inverted_reflect_xaxis(8)
#super_mario_create_sandglass(20)
#super_mario_create_diamond(20)
super_mario_petronas_tower(30)
#super_mario_shriti_shodh(60)

input('')




