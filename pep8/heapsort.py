#!/usr/bin/env python3
#Build max heap from input
  #Max Heap: tree satisfying property that if P is parent node of C, value of P >= value of C
  #Node at top is largest value
#Creating heap stores largest item at root of heap. Swap first and last element.
#Reduce heap size by 1 (omitting final element, now sorted)
#heapify things
#Repeat while heap size > 1
"""
well-named file.  see first function's name too
"""

import random

SHOW_LISTS = False

#TODO - Bottom-up heapsort

def heapsort(seq):
    """
    it's heapsort!
    """
    length = len(seq)

    #Go from end to start
    #Everything in order when gets to next set
    for x in range(length, -1, -1):
        build_heap(seq, length, x)

    for x in range(length-1, 0, -1):
        tmp = seq[0]
        seq[0] = seq[x]
        seq[x] = tmp

        #Leaving end alone, make re-heap everything
        #Only root changed, only need to re-heap root
        #Don't use x-1 b/c x is index, so 1 less than length already
        build_heap(seq, x, 0)

    return seq

#Notes:
#Binary tree - a tree in which each node has at most two children - left child and right child
#In zero-based array:  left_child = 2*index + 1, right_child = 2*index + 2
#             0
#       1           2
#     3   4     5     6
#    7 8 9 10 11 12 13 14
#Binary heap - a heap data structure, takes form of binary tree.  Fulfills two extra poperties
#  1 - Shape Property: Is complete binary tree.  All levels (maybe except final) are completely full
#  2 - Heap  Property: The value of each node >= or <= than the value of both children
#If parents >=, called a max heap.  <= are min heaps
#Creating max-heap puts largest item at start
#   Heapsort - make heap, move first item to end, repeat with one fewer pieces
#Creating min-heap puts smallest item at start
#   Heapsort - make heap, move up one level, repeat

#Creating heap
#Inputs - sequence (seq), heap size (siz), presumptive largest (root)

def build_heap(seq, siz, root):
    """
    function to heapify a path down a tree
    """
    #track largest
    largest = root

    #check for right and left children
    left = 2*largest + 1
    right = 2*largest + 2

    #if exist and larger, swap
    if left < siz and seq[left] > seq[largest]:
        largest = left
    if right < siz and seq[right] > seq[largest]:
        largest = right

    if root != largest:
        temp = seq[root]
        seq[root] = seq[largest]
        seq[largest] = temp
        #Recursively make sure all leaves follow heap property
    build_heap(seq, siz, largest)

def main():
    """
    ... runs a heapsort
    """
    #length = random.randint(100000, 1000000000)
    length = 10000
    seq = [random.randint(0, 1000) for i in range(length)]
    if SHOW_LISTS:
        print(seq)
    heapsort(seq)
    if SHOW_LISTS:
        print(seq)

if __name__ == '__main__':
    main()
