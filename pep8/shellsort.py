#!/usr/bin/env python3
"""
Generalized insertionsort
Allows swaps not next to each other
"""

import random

SHOW_LISTS = False

def shellsort(seq):
    """ A shellsort with wikipedia-recommended gaps """
    gaps = [701, 301, 132, 57, 23, 10, 4, 1]
    for gap in gaps:
        #From first potential swap going up
        for x in range(gap, len(seq)):
            #print(seq)
            #Store value in case of swap
            temp = seq[x]
            #Set y equal to x
            y = x
            #For each value of y greater than gap min where the lower value is greater
            while y >= gap and seq[y-gap] > temp:
                #Set the first value later
                seq[y] = seq[y-gap]
                #Set y one value less and do over
                y -= gap
            #Once loop breaks, set that value as temp, the lowest encountered
            seq[y] = temp

def main():
    """ A function to run a shellsort """
    #length = random.randint(100000,1000000000)
    length = 30
    seq = [random.randint(0, length) for i in range(length)]
    if SHOW_LISTS:
        print(seq)
    shellsort(seq)
    if SHOW_LISTS:
        print(seq)

if __name__ == '__main__':
    main()
