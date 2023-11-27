def in1020(a,b):
    if 10 <= a <= 20:
        return True
    elif 10 <= b <= 20:
        return True
    else:
        return False
    
def squirrel_play(temp, is_summer):
    if is_summer:
        if 60 <= temp <= 100:
            return True
        else:
            return False
    else: # not summer
        if 60 <= temp <= 90:
            return True
        else:
            return False
            

print(squirrel_play(70,True))



def cigar_party(cigars, is_weekend):

    if is_weekend and cigars >= 40:
        return True
    elif not is_weekend and cigars >= 40 and cigars <= 60:
        return True
    else:
        return False

