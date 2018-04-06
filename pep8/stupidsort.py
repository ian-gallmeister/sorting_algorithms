#!/usr/bin/env python3
"""
stupidsort/gnomesort
"""

import random

SHOW_LISTS = False

def stupidsort(seq):
    """
    gnome sort/stupid sort
    """
    x = 0
    while x < len(seq):
        if x == 0:
            x += 1
        elif seq[x] >= seq[x-1]:
            x += 1
        else:
            seq[x], seq[x-1] = seq[x-1], seq[x]
            x -= 1

def main():
    """
    run a stupidsort
    """
    #length = random.randint(100000, 1000000000)
    length = 10000
    seq = [random.randint(0, length) for i in range(length)]
    if SHOW_LISTS:
        print(seq)
    stupidsort(seq)
    if SHOW_LISTS:
        print(seq)

if __name__ == '__main__':
    main()
