#!/usr/bin/env python3
#Go up list
#If current item is larger than the next item, swap them
#At end of passthrough, largest item at top
#Repeat going one fewer until reach the end

import random

SHOW_LISTS=False

def bubblesort( to_sort ):
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
def sort( seq ):
  for x in range(len(seq)):
    for y in range(len(seq)-1,i,-1):
      if seq[y] < seq[y-1]:
        tmp = seq[y]
        seq[y] = seq[y+1]
        seq[y+1] = tmp
      #print( '{} - pass_number={}, list_index={}'.format(seq, x, y) )
  return seq

def main():
  #length = random.randint(100000,1000000000)
  length = 10000
  unsorted = [ random.randint(0,1000) for i in range(length) ]
  if SHOW_LISTS:
    print( unsorted )
  bubblesorted = bubblesort( unsorted )
  if SHOW_LISTS:
    print( bubblesorted )

if __name__ == '__main__':
  main()
