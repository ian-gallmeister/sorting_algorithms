#!/usr/bin/env python3
""" An implementation of radixsort """

import random

SHOW_LISTS = True

def radixsort(seq):
    """ The radix sort algorithm """
    max_val = max(seq)
    oom = 0 #order of magnitude
    while max_val // 10**oom > 0:
        countingsort(seq, oom)
        oom += 1

#adapt to take arg for which digit to use
def countingsort(seq, oom):
    """ Countingsort adapted for radix sorts needs """
    count_array = [0]*10 #decimal integer sort so only 10 digits
    output_array = [0]*len(seq)
    for val in seq:
        newval = (val % 10**(oom+1))//(10**oom)
        count_array[newval] += 1
    for _ in range(1, 10): #decimal inegers
        count_array[_] += count_array[_-1]
    posn = len(seq) - 1
    while posn >= 0:
        newval = (seq[posn] % 10**(oom+1))//(10**oom)
        output_array[count_array[newval]-1] = seq[posn]
        count_array[newval] -= 1
        posn -= 1
    seq[0:] = output_array

def main():
    """ Running radixsort for timing and whatever """
    #length = random.randint(100000,1000000000)
    length = 25
    seq = [random.randint(0, 1000) for i in range(length)]
    if SHOW_LISTS:
        print(seq)
    radixsort(seq)
    if SHOW_LISTS:
        print(seq)

if __name__ == '__main__':
    main()
