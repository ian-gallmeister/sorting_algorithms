#!/usr/bin/env python3
#Go up list
#If current item is larger than the next item, swap them
#At end of passthrough, largest item at top
#Repeat going one fewer until reach the end
"""
This is bubblesort.  The file is well named
"""

import random

SHOW_LISTS = False

def bubblesort(to_sort):
    """
    Basic bubblesort implementation.  Top down.
    """
    for final_position in range(len(to_sort)-1, 0, -1):  #len-1 so don't leave list
        for x in range(final_position):
            if to_sort[x] > to_sort[x+1]:
                temp = to_sort[x]
                to_sort[x] = to_sort[x+1]
                to_sort[x+1] = temp
    return to_sort

#Need to record each position swap as well
#Moves smallest to the left, progressively
#stops checking lowest as goes
def sort(seq):
    """
    Basic bubblesort implementation.  Bottom up.
    """
    for x in range(len(seq)):
        for y in range(len(seq)-1, x, -1):
            if seq[y] < seq[y-1]:
                tmp = seq[y]
                seq[y] = seq[y+1]
                seq[y+1] = tmp
    return seq

def main():
    """
    Wrap function to perform a bubblesort.  Uses top down
    """
    #length = random.randint(100000,1000000000)
    length = 10000
    unsorted = [random.randint(0, 1000) for i in range(length)]
    if SHOW_LISTS:
        print(unsorted)
    bubblesorted = bubblesort(unsorted)
    if SHOW_LISTS:
        print(bubblesorted)

if __name__ == '__main__':
    main()
