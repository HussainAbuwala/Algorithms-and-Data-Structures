'''
        NAME: HUSSAIN SADIQ ABUWALA
        STUDENT-ID: 27502333

'''
def my_z_box(input_string):
    # initialize the array
    my_z_array = [0] * len(input_string)
    my_z_array[0] = len(input_string)
    # initialize the box boundary
    my_left = 0
    my_right = 0
    # loop through the string, skipping 0
    i = 1
    while (i < len(input_string)):
        # if outside the z-box, then we need to my_count
        if i > my_right:
            my_count = keep_track_prefix(input_string,i)
            # set the z-value at i
            my_z_array[i] = my_count
            # if there is a box, update the box boundary
            if my_count > 0:
                my_left = i
                my_right = i + my_count - 1
        # if it is within the box
        # i <= my_right
        else:
            # get the paired prefix index (z-value) to copy
            index_prefix = i - my_left
            # the my_remaining length of the box
            my_remaining = my_right - i + 1
            # case 2a
            if my_z_array[index_prefix] < my_remaining:
                # copy the value
                my_z_array[i] = my_z_array[index_prefix]
            # case 2b

            elif my_z_array[index_prefix] == my_remaining:
                new_right = find_new_right(my_right,input_string,i)
                # update the z-array with the extension
                my_z_array[i] = new_right - i
                # new my_left and my_right boundary
                my_left = i
                my_right = new_right - 1
            # case 2c

            else:
                my_z_array[i] = my_remaining

        i+=1
    # return the z-array
    return my_z_array


def find_new_right(my_right,input_string,i):
    new_right = my_right + 1
    while new_right < len(input_string) and input_string[new_right] == input_string[new_right - i]:
        new_right += 1
    return new_right


def keep_track_prefix(input_string,i):
    my_count = 0
    # while we are still within the string
    # and the letter is the same as the prefix
    # note: my_count keep track of the prefix
    while i + my_count < len(input_string) and input_string[my_count] == input_string[i + my_count]:
        # increment my_count
        my_count += 1

    return my_count


def my_run():
    # the input
    my_string = "abaabcab"
    # testing the z-algorithm
    my_z_array = my_z_box(my_string)

    print(my_z_array)

if __name__ == "__main__":
    pass
