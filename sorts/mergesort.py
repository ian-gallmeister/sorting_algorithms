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
    print(seq)
    #int() acts as floor function.  truncates any decimals
    middle = int( end + (start-end)/2 )

    #Sort left
    print('mergesort( seq, {st}, {md} )'.format(st=start,md=middle))
    mergesort( seq, start, middle )
    #Sort right
    #Not incrementing middle b/c middle previously is length() so only goes to middle-1
    #Now middle is first index so need that value
    mergesort( seq, middle, end )
    print( 'mergesort( seq, {md}, {end} )'.format(md=middle,end=end) )

  #Merge
  if end - start == 1:
    pass
  else:
    merge( seq, start, middle, end )

def merge( seq, start, middle, end ):
  #Create new array for sorted piece
  merged = []
  #Replace seq with that
  subarray_one = list(seq[start:middle])
  subarray_two = list(seq[middle:end])
  while len(subarray_one) > 0 or len(subarray_two) > 0:
    if len(subarray_one) == 0:
      if len(subarray_two) == 0:
        break
      else:
        merged = list( merged + subarray_two )
        subarray_two = []
    elif len(subarray_two) == 0:
      if len(subarray_one) == 0:
        break
      else:
        merged = list( merged + subarray_one )
        subarray_one = []
    else:
      if subarray_one[0] <= subarray_two[0]:
        merged.append( subarray_one.pop(0) )
      else:
        merged.append( subarray_two.pop(0) )
  seq[start:end] = merged

def main():
  #length = random.randint(100000,1000000000)
  length = 10000
  seq = [ random.randint(0,length) for i in range(length) ]
  if SHOW_LISTS:
    print( seq )
  mergesort( seq )
  if SHOW_LISTS:
    print( seq )

if __name__ == '__main__':
  main()
