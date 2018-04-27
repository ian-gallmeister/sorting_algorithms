#!/usr/bin/env python3
""" An implementation of countingsort used to learn it for radixsort """

import random

SHOW_LISTS = False

def countingsort(seq):
    """ A countingsort implementation """
    max_val = max(seq)
    print(seq)
    print('Min: {}'.format(min(seq)))
    print('Max: {}'.format(max_val))

    #Need an index for each potential value
    count_array = [0]*(max_val+1) #0 to max_val
    output_array = [0]*len(seq)
    print(count_array)

    #How many items of each value are there?  Store answer at index
    for val in seq:
        count_array[val] += 1
    print(count_array)

    #Now how many items less than or equal to index are there.  Store again at index
    for _ in range(1, max_val+1): #0 already done
        count_array[_] += count_array[_-1]
    print(count_array)

    #Sort the thing.  Somehow
    for val in seq:
        output_array[count_array[val]-1] = val
        count_array[val] -= 1
    print(output_array)

    seq = output_array

def main():
    """ Run a countingsort """
    #length = random.randint(100000,1000000000)
    length = 40
    seq = [random.randint(0, 50) for i in range(length)]
    if SHOW_LISTS:
        print(seq)
    countingsort(seq)
    if SHOW_LISTS:
        print(seq)

if __name__ == '__main__':
    main()

#seq: [7,9,6,3,2,5,1,6,3,2,9,4,3,5]               #series of numbers
#       val:     0, 1, 2, 3, 4, 5, 6, 7, 8, 9
#count_array:   [0, 1, 2, 3, 1, 2, 2, 1, 0, 2]    #num times each number appears (value is index)
#count_arr_sum: [0, 1, 3, 6, 7, 9, 11,12,12,14]   #number of elements less than or equal to value
#In empty list, length of seq, start putting in values
#Iterate through sequence
#For value in seq, find number of items less than or equal to it
#Place value there, reduce the number less than or equal by one
    #This makes the other equivalent values slot in until they fill all the spots for them
