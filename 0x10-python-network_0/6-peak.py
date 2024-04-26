#!/usr/bin/python3
"""Finds a peak in a list of unsorted integers"""

def find_peak(list_of_integers):
    
    # Check if the list is None or empty
    if list_of_integers is None or len(list_of_integers) == 0:
        return None
    
    # Initialize variables for binary search
    lo = 0
    hi = len(list_of_integers) - 1

    # Binary search loop
    while lo < hi:
        # Calculate the midpoint
        mid = lo + (hi - lo) // 2

        # Check if the midpoint is less than the next element
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            lo = mid + 1
        else:
            hi = mid

    # At the end of the loop, lo will point to a peak
    return list_of_integers[lo]
