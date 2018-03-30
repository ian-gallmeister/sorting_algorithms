#!/usr/bin/env python3
#If current item is larger than the next item, swap them
#At end of passthrough, largest item at top
#Then reverse.  If current item is smaller than next, swap them
#At end of passthrough, smallest item on bottom
#Repeat going one fewer each time until reach end

import random

def cocktailshaker( to_sort ):
  #Determined by testing cause I'm lazy
  largest = len(to_sort) + 2
  smallest = 0
  while largest >= smallest:
    #Sort up
    for x in range( smallest-2, largest ):
    #Adjust end
    largest -= 1

    #Sort down
    for smallest in range( largest-2, smallest, -1 ):
    #Adjust start
    smallest += 1
    
  return to_sort

#Need to record each position swap as well
#Moves smallest to the left, progressively 
#stops checking lowest as goes


if __name__ == '__main__':
  main()

def main():
  length = random.randint(100000,1000000000)
  length = 100
  unsorted = [ random.randint(0,1000) for i in range(length) ]
  cocktailshaken = cocktailshaker( unsorted )

if __name__ == '__main__':
  main()


def bubblesort( to_sort ):
  for final_position in range(len(to_sort)-1, 0, -1):  #len-1 so don't leave list
    for x in range(final_position):
      if to_sort[x] > to_sort[x+1]:
        temp = to_sort[x]
        to_sort[x] = to_sort[x+1]
        to_sort[x+1] = temp
  return to_sort
