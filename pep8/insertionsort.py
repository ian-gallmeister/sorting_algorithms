#!/usr/bin/env python3
#Start at bottom going up
#From start, go down
#Swap if current smaller than next lower
"""
pep8 wants this.  it's pretty self-explanatory
"""

import random

SHOW_LISTS = False

def insertionsort(seq):
    """
    an insertionsort implementation
    """
    #Can't start at 0, nothing lower
    for x in range(1, len(seq)):
        #Stop one higher than end so don't go off end of list
        for y in range(x, 0, -1):
            if seq[y] < seq[y-1]:
                seq[y], seq[y-1] = seq[y-1], seq[y]

def isort(seq):
    """
    two line insertionsort
    """
    for i in [y for x in range(1, len(seq)) for y in range(x, 0, -1)]:
        if seq[i] < seq[i-1]: seq[i], seq[i-1] = seq[i-1], seq[i]


def main():
    """
    runs an insertionsort
    """
    #length = random.randint(100000,1000000000)
    length = 10000
    seq = [random.randint(0, length) for i in range(length)]
    if SHOW_LISTS:
        print(seq)
    insertionsort(seq)
    if SHOW_LISTS:
        print(seq)

if __name__ == '__main__':
    main()
