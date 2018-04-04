#!/usr/bin/env python3
#Pick an element (a pivot)
#Reorder array so all elements with values < pivot before, all elements > pivot come after
#Recursively apply to the two resulting pieces until pieces all length 1

#Recursion
#Base Case: sizes 1 and 0, ordered by default, extends from there

#Several methods pivot selection + partition steps
#  Choice of implementation can affect performance
##Lomuto Parition scheme
##Pros: Simple
##Cons: Devolves to O(n^2) if already sorted
##Chooses pivot, typically final element in array

##Hoare Partition scheme
##Original scheme
##Uses indices at end, moving inwards until inverts
##Typically uses 3x fewer swaps
##Devolves to O(n^2) if already sorted
##Guarantees nonzero partitions non=infinite recursion

#Implementation problems
#Pivot Choice --
#  Leftmost element causes worst-case scenario if already sorted
#  Solution: random index, middle index, or median of first, middle, last element
#    Median of three counters sorted/reverse sorted output
#      Also gets closer to actual median value than any single element
#    Can also go for the ninther - take median of three for first, second, third of array.  Then take median of those three
#Repeated Elements --
#  Lots of repeated elements slow quicksort a lot

#Optimizations
#  Recursion to smaller side first.  It sorts itself, then goes to the larger piece
#  Once reach threshold, use a different sort that needs fewer swaps

#Parallelization
#  Good candidate for parallelization
#  Can have disadvantages depending on pivot choices

import random

SHOW_LISTS=False
PIVOT = 'random'
#random | traditional
PARTITION='hoare'
# hoare | lomuto

def quicksort( seq, low, high ):
  if PARTITION == 'lomuto':
    lomuto( seq, low, high )
  elif PARTITION == 'hoare':
    hoare( seq, low, high )

def hoare( seq, low, high):
  if low < high:
    sep = hor_partition( seq, low, high )  
    #print( seq )
    # Separation not exactly in right spot, must keep sorting those same spots
    hoare( seq, low, sep )
    hoare( seq, sep+1, high )

def hor_partition( seq, low, high ):
  #First element is pivot.  Gets bounced around as elements move around it until all lower to left and all higher to right
  if PIVOT == 'random':
    pivot = seq[random.randint(low,high)]
  elif PIVOT == 'traditional':
    pivot = seq[low]
  #print( 'Pivot: {} -> {}'.format(low, pivot) )
  low_index = low 
  high_index = high  
  while True:
    #Scan from end towards start
    #Stop at first element lower than or equal to pivot
    while seq[high_index] > pivot:
      high_index -= 1
    #Scan from start towards end
    #Stop at first element greater than or equal to pivot (which is the pivot)
    while seq[low_index] < pivot:
      low_index += 1
    #Assuming first element too large before first element too small, swap 'em
    #Then do it again
    if low_index < high_index:
      seq[high_index],seq[low_index] = seq[low_index],seq[high_index]
      #Move further inwards (in case of repeated values messing things up)
      high_index -= 1
      low_index += 1
      #print( seq )
    #Once you cross each other to find the pieces that don't work, list is partitioned
    #Return right below that in-between point
    else:
      #print ( seq )
      return high_index

def lomuto( seq, low, high ):
  if low < high:
    sep = lom_partition( seq, low, high )
    #print( seq )
    #Location of pivot returned.  quicksort the two pieces on either side
    lomuto( seq, low, sep - 1 )
    lomuto( seq, sep + 1, high )

def lom_partition( seq, low, high ):
  #Final element value is pivot
  if PIVOT == 'random':
    pivot = seq[random.randint(low,high)]
  elif PIVOT == 'traditional':
    pivot = seq[high]
  #print( 'Pivot: {} -> {}'.format(high, pivot) )
  #Separator index starts at lowest index
  sep = low - 1

  #Go through ALL elements.  pseudocode goes to high-1.  range() does that automatically
  #Stoopid ian
  for x in range(low, high):
    #For too-low values
    if seq[x] < pivot:
      #line up below-pivot values from the left
      sep += 1
      seq[sep],seq[x] = seq[x],seq[sep]

  #place pivot value one right of the lesser values lined up to the left and return that index
  seq[sep+1],seq[high] = seq[high],seq[sep+1]
  return sep+1

def main():
  #length = random.randint(100000,1000000000)
  length = 10000
  seq = [ random.randint(0,1000) for i in range(length) ]
  if SHOW_LISTS:
    print( seq )
  quicksort( seq, 0, len(seq)-1 )
  if SHOW_LISTS:
    print( seq )

if __name__ == '__main__':
  main()
