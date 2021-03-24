from solve_n_queens import print_board
def naive_approach_knap_bounded(values,weights,capacity):
       return _aux_naive_approach_knap(values,weights,capacity,0,0,0)


def naive_approach_knap_unbounded(values, weights, capacity):
    return _aux_naive_approach_knap_unbounded(values, weights, capacity, 0, 0, 0)


def _aux_naive_approach_knap(values,weights,capacity,temp_c,temp_v,i):

    if temp_c > capacity:
        return float('-inf')
    if i >= len(values):
        return temp_v
    else:
        return max(_aux_naive_approach_knap(values,weights,capacity,weights[i] + temp_c,values[i] + temp_v,i + 1 ),
                   _aux_naive_approach_knap(values, weights, capacity,temp_c,temp_v, i + 1))

def _aux_naive_approach_knap_unbounded(values,weights,capacity,temp_c,temp_v,i):

    if temp_c > capacity:
        return float('-inf')
    if i >= len(values):
        return temp_v
    else:
        return max(_aux_naive_approach_knap_unbounded(values,weights,capacity,weights[i] + temp_c,values[i] + temp_v,i),
                   _aux_naive_approach_knap_unbounded(values, weights, capacity,temp_c,temp_v, i + 1))


def integer_knapsack_dp(wt,val,W):

    '''
    
    
    Recurrence Relation:
                -----------------------------------------------------------
                |
                |0 if i=0,M=0 (if no items or capacity is 0)
                |
    C[i][M] =   |C[i-1][M] of w[i] > M (if weight of item exceeds capacity,take previous subproblem)
                |
                |max(v[i] + C[i-1][M-w[i]],C[i-1][M]) if i>0 and w[i] < M 
                 -----------------------------------------------------------

    
    :param wt: 
    :param val: 
    :param W: 
    :return: 
    '''



    dp_table = []
    wt.insert(0,None)
    val.insert(0,None)

    for i in range(len(val)):
        dp_table.append([None] * (W+1))


    for i in range(len(dp_table)):
        dp_table[i][0] = 0

    x = dp_table[0]


    for i in range(len(x)):
        x[i] = 0


    for i in range(1,len(dp_table)):
        for j in range(len(dp_table[i])):
            if wt[i] > W:
                dp_table[i][j] = dp_table[i-1][j]
            else:
                dp_table[i][j] = max(val[i] + dp_table[i-1][j - wt[i]],dp_table[i-1][j])

    return dp_table[len(val)-1][W]

if __name__ == '__main__':
    wt = [10, 20, 30]
    val = [60, 100, 120]
    W = 50
    n = len(val)
    print(integer_knapsack_dp(wt,val,W))
