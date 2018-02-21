from time import time
from functools import partial

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
    
def naive(a, b):
    total = a
    for i in range(b-1):
        total *= a
    return total
    
def timer(function):
    start = time()
    function()
    return time() - start

a = 999
b = 999
naive = partial(naive, a, b)
ours = partial(fast_exp, a, b)
theirs = partial(pow, a, b)
print(timer(naive))
print(timer(ours))
print(timer(theirs))
