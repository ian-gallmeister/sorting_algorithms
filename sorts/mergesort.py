#!/usr/bin/env python3
#Divide unsorted into 'n' sublists, each with 1 element
#Merge sublists over and over until just one sublist
##OR##
#Split list into two
#Mergesort left
#Mergesort right
#Merge the two sorted pieces

import random

SHOW_LISTS=False

def mergesort( seq, start, end ):
  if end - start > 1:
    #print(seq)
    #int() acts as floor function.  truncates any decimals
    middle = int( end + (start-end)/2 )

    #Sort left
    #print('mergesort( seq, {st}, {md} )'.format(st=start,md=middle))
    mergesort( seq, start, middle )
    #Sort right
    #Not incrementing middle b/c middle previously is length() so only goes to middle-1
    #Now middle is first index so need that value
    mergesort( seq, middle, end )
    #print( 'mergesort( seq, {md}, {end} )'.format(md=middle,end=end) )

  #Merge
  if end - start == 1:
    pass
  else:
    merge( seq, start, middle, end )

def merge( seq, start, middle, end ):
  merged = []
  index_l = index_r = 0
  left_array = list(seq[start:middle])
  right_array = list(seq[middle:end])

  while index_l < len(left_array) and index_r < len(right_array):
    if left_array[index_l] <= right_array[index_r]:
      merged.append( left_array[index_l] )
      index_l += 1
    else:
      merged.append( right_array[index_r] )
      index_r += 1 

  merged += left_array[index_l:]
  merged += right_array[index_r:]
  
  seq[start:end] = merged

def main():
  #length = random.randint(100000,1000000000)
  length = 10000
  seq = [ random.randint(0,length) for i in range(length) ]
  if SHOW_LISTS:
    print( seq )
  mergesort( seq, 0, len(seq) )
  if SHOW_LISTS:
    print( seq )


if __name__ == '__main__':
  main()
