def non_unique_partitions(user_input):
    return _aux_partitions(user_input,0," ")

def _aux_partitions(match,total,string):
    if total == match:
        print(string)
        return 1
    elif total > match:
        return 0
    else:

        return _aux_partitions(match, total + 1, str(1) + ' ' + string) + _aux_partitions(match, total + 2, str(2) + ' ' + string)


print("The number of non-unique partitions are: " + str(non_unique_partitions(5)))