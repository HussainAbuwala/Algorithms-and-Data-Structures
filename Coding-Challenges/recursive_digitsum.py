def recur_digitsum(digits):
    if len(digits) ==0:
        return 0
    else:
        return int(digits[0]) + recur_digitsum(digits[1:len(digits)])


def digit_sum_tail_recur(digits):
    return digit_sum_tail_helper(0,digits)

def digit_sum_tail_helper(acc,digits):
    if len(digits)==0:
        return acc
    else:
        return digit_sum_tail_helper(acc + int(digits[0]),digits[1:len(digits)])


def cal_digital_root_itr(digits):
    i = len(digits)
    while (i !=1):
        digits = str(recur_digitsum(digits))
        i = len(digits)

    return digits

def cal_digital_root_rec(digits):
    if len(digits) == 1:
        return digits
    else:
        digits = str(digit_sum_tail_recur(digits))
        return cal_digital_root_rec(digits)


user_input = input('Enter digits: ')
print(cal_digital_root_rec(user_input))