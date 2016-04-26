def fast_exp(a, b):
    if b < 0:
        return 1 / fast_exp(a, -b)

    ans = 1
    cumulative = a
    counter = 1

    while counter <= b:
        if b & counter > 0:
            ans *= cumulative
        
        cumulative *= cumulative
        counter <<= 1
    
    return ans