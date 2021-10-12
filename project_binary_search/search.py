import math


def binary_search(l, target, low =None, high = None):
    
    # setting base values on first iteration
    if low is None:
        low = 0
    if high is None:
        high = len(l)-1
    
    # failsafe if the list doesnt cointains the target
    if high<low:
        return -1
    
    # midpoint = len(l)//2
    midpoint = math.floor((low+high)/2)

    if target == l[midpoint]:
        return midpoint
    elif target > l[midpoint]:
       return binary_search(l, target ,midpoint+1, high)
    else:
       return binary_search(l, target, low, midpoint-1)