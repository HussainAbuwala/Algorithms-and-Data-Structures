def word_break_problem(s,dict):
    result = _aux_word_break(s,dict)
    if result == 1:
        return True
    return False

def _aux_word_break(s,dict):
    if len(s) == 0:
        return 1

    else:
        r = 0
        for i in range(1,len(s)+1):
            if s[:i] in dict:
                r = max(r,_aux_word_break(s[i:len(s)],dict))
            else:
                r = max(r,0)

    return r

print(word_break_problem('ilike',['i','like','sam','sung']))
