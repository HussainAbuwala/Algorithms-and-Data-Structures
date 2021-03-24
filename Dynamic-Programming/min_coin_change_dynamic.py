def coin_change_ways(coins,sum):
    return int(_count_aux(coins,sum,len(coins)-1,{}))

def _count_aux(arr,sum,index,hashtable):

    if (str(sum) + '-' + str(index)) in hashtable:
        return hashtable[str(sum) + '-' + str(index)]
    elif sum < 0:
        return float('inf')
    elif index == 0 and sum % arr[index] == 0:
        return (sum / arr[index])
    elif index == 0 and sum % arr[index] != 0:
        return float('inf')
    else:
        total_ways = _count_aux(arr,sum,index-1,hashtable)

        i = 1
        save_sum = sum
        while sum >0:
            total_ways = min(total_ways,i + _count_aux(arr, sum-arr[index], index - 1,hashtable))
            sum = sum - arr[index]
            i+= 1

        hashtable[str(save_sum) + '-' + str(index)] = total_ways

        return total_ways

print(coin_change_ways([1,5,6,9],13))