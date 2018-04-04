#!/usr/bin/env python3

import random

SHOW_LISTS=False

def insertionsort( seq ):
  return seq

def main():
  #length = random.randint(100000,1000000000)
  length = 10000
  seq = [ random.randint(0,1000) for i in range(length) ]
  if SHOW_LISTS:
    print( seq )
  seq = bubblesort( seq )
  if SHOW_LISTS:
    print( seq )

if __name__ == '__main__':
  main()
