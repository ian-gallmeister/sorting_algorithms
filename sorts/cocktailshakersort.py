#!/usr/bin/env python3
#If current item is larger than the next item, swap them
#At end of passthrough, largest item at top
#Then reverse.  If current item is smaller than next, swap them
#At end of passthrough, smallest item on bottom
#Repeat going one fewer each time until reach end

import random

def setup():
  seq = []
  for x in range(11,0,-1):
    seq.append(x)
  seq
  return seq

def cocktailshaker( to_sort ):
  #Determined by testing cause I'm lazy
  largest = len(to_sort) - 1 #adjust indices for lists
  smallest = 0
  while True:
    #Sort up.
    for x in range( smallest, largest ):
      if to_sort[x] > to_sort[x+1]:
        temp = to_sort[x]
        to_sort[x] = to_sort[x+1]
        to_sort[x+1] = temp
    #Adjust end
    largest -= 1
    if largest <= smallest:
      break

    #Sort down.  
    for x in range( largest, smallest, -1 ):
      if to_sort[x] < to_sort[x-1]:
        temp = to_sort[x]
        to_sort[x] = to_sort[x-1]
        to_sort[x-1] = temp
    #Adjust start
    smallest += 1
    if largest <= smallest:
      break
    
  return to_sort

#Need to record each position swap as well
#Moves smallest to the left, progressively 
#stops checking lowest as goes

def main():
  length = random.randint(100000,1000000000)
  length = 10000
  unsorted = [ random.randint(0,1000) for i in range(length) ]
  cocktailshaken = cocktailshaker( unsorted )

if __name__ == '__main__':
  main()
