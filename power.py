def rec_pow(base, tavan):
    if tavan == 0:
        return 1
    else:
        return base * rec_pow(base, tavan - 1)
        
#power= rec_pow(2,3)
#print(power)