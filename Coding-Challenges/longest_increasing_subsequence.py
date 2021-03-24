def longest_increasing_subs(arr):
    return _aux_longest_incr_subs(float('-inf'),arr,0)

def _aux_longest_incr_subs(previous,arr,index):
    if index >= len(arr):
        return 0
    else:
        r = float('-inf')
        if arr[index] > previous:
            r = 1 + _aux_longest_incr_subs(arr[index],arr,index+1)
        return max(r,_aux_longest_incr_subs(previous,arr,index+1))


print(longest_increasing_subs([10,9,8,8.5]))