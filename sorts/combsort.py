#!/usr/bin/env python3
# Improvement on bubblesort
#Idea is to eliminate turtles - low values near the end of the list
#Compare gaps, gap shrinking by 1.3 each time - empirically calculated most efficient value

import random

SHOW_LISTS=True

def combsort( seq ):
  size = len(seq)
  gap = len(seq)
  shrink = 1.3
  complete = False

  while not complete:
    gap = int(gap/shrink)
    if gap <= 1:
      gap = 1
      complete = True #Turned false if any swaps happen
  
    index = 0
    while index + gap < size:
      if seq[index] > seq[index+gap]:
        seq[index],seq[index+gap]=seq[index+gap],seq[index]
        complete = False
      index += 1

def main():
  #length = random.randint(100000,1000000000)
  length = 1000
  seq = [ random.randint(0,1000) for i in range(length) ]
  if SHOW_LISTS:
    print( seq )
  combsort( seq )
  if SHOW_LISTS:
    print( seq )

if __name__ == '__main__':
  main()
