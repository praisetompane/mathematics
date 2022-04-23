
def _have_same_sign(number_1, number_2):
    if number_1 < 0 and number_2 < 0: return True
    elif number_1 > 0 and number_2 > 0: return True
    else: False

def _is_negative(number): return number < 0
    
def _largest_number_sign(number_1, number_2):
    if abs(number_1) > abs(number_2):
        if _is_negative(number_1): return -1
        else: return 1
    else: 
        if _is_negative(number_2) < 0: return -1
        else: return 1

def add_integers(number_1, number_2):
    if number_1 == 0: return number_2
    elif number_2 == 0: return number_1
    elif(_have_same_sign(number_1, number_2)):
        return number_1 + number_2 #gather the 2 sets of ones into one set, count how many ones you have 
    else:
        return (abs(number_1) - abs(number_2)) * _largest_number_sign(number_1, number_2)
        #gather the 2 sets of ones into one set, count how many ones you have 
        #convert the sign of the ones to the type(negative or positive) of the ones which had a higher count.



