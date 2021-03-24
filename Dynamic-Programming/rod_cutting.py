def naive_rod_cutting(rods,n):

    if n == 1:
        return rods[1]
    else:
        maximum_rev = float('-inf')
        for i in range(1,n):
            maximum_rev = max(maximum_rev,naive_rod_cutting(rods,i) + naive_rod_cutting(rods,n-i))

        return max(maximum_rev,rods[n])


def rod_cutting_dp(rods,n):

    """
    
    
    Recurrence Relation:
    
    However, if you had written it as...
    
                +--
                |   P[i]
    C[i] = max -|
                |
                |   max (C[j] + C[i-j]) for all 1<=j<=i-1
                +--

    
    :param rods: 
    :param n: 
    :return: 
    """


    dp_table = [None] * (n+1)
    dp_table[1] = rods[1]
    for i in range(2,n+1):
        maximum_rev = float('-inf')
        for j in range(1,i):
            maximum_rev = max(maximum_rev,dp_table[j] + dp_table[i-j])
        dp_table[i] = max(rods[i],maximum_rev)

    return dp_table[n]


if __name__ == '__main__':
    #print(naive_rod_cutting([0,3,5,8,9,10,17,17,20],8))
    print(rod_cutting_dp([0,2,5,7,8],4))