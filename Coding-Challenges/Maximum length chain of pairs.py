def max_length_chain(chain):
    return _aux_max_length_chain([0,float('-inf')],chain)

def _aux_max_length_chain(previous,chain):
    if len(chain) == 0:
        return 0
    else:
        r = float('-inf')
        if chain[0][0] > previous[1]:
            r = 1 + _aux_max_length_chain(chain[0],chain[1:])
        r = max(r,_aux_max_length_chain(previous,chain[1:]))
        return r

print(max_length_chain([[5,24],[39,60],[15,28],[50,90]]))