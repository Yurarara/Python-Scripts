import math
import random
from Stack import *
# After discussing O(N^2) sorting, we move onto O(Nlog(N)) algorithms. These algorithms perform better (faster) for
# larger amount of values. (e.g. for N=1000, N^2 would be 10^6, but Nlog(N) is smaller than 10^4 - that's 100 times
# faster.) This difference in speed makes O(Nlog(N)) algorithms more practical and hence more widely applied.

# Heap Sorting: this algorithm is paired with a specific data structure, namely the heap. A heap is by its nature a
# complete binary tree. A tree is binary in that all of its nodes have at most 2 children. A tree is complete in that
# all of its levels are filled except the last.
# If the last level is not filled, all values in this level are stored on the left side of the tree.
# A heap is a specific form of complete binary trees, that for all nodes, their children are not larger than themselves.

# It also includes the method for storing a complete binary tree in an array. The projection is based on the following
# 2 relationships.
# Given that the tree's root is at index 0:
# 1. the children nodes of the i-th node is positioned at indices 2*i+1 and 2*i+2.
# 2. conversely, the parent node of the j-th node is (j-1)/2, floored.
# Specifically, if a node's index in its tree surpasses the length of the array, it implies that there is no such node
# in the tree.

# A heap is by its nature a complete binary tree. It's worth noticing that, when adding a value to a heap, the new value
# should always be positioned first at the bottom level, right next to the last value of that level. (When a heap is
# stored in the form of an array, this is automatically guaranteed.) Then, it should be moved upwards along the tree to
# the final position according to its magnitude. (The parent node should always be equal or larger than its children.)


# The following code is the method of transforming an array to a heap.
# NOTICE: the output of this method only guarantees that the heap follows the definition of a complete binary tree. For
# lists with same values but in different order, the result may be different.
def make_heap(values):
    # add values into a heap by order.
    for i in range(0, len(values)):
        index = i
        '''move the value upwards the tree'''
        while index != 0:
            '''search for the index of its parent node'''
            parent = math.floor((index - 1) / 2)
            '''if the child value is smaller or equal to the parent value (i.e. correctly positioned)'''
            if values[index] <= values[parent]:
                break
            temp = values[index]
            values[index] = values[parent]
            values[parent] = temp
            '''go upwards, check again'''
            index = parent


# Because of the structural feature of a heap, it's much suitable for constructing a priority queue, whose entries are
# returned in the priority order. For heaps, it means to return and remove the root (largest among all values).
# In that case, the first thing to consider is how to maintain the structure of the heap: a complete binary tree - when
# the root is removed, the structure of a tree collapses. A smart way of doing this is to move the last value in the
# tree to its top as its new root. Then, this root value will move downwards along the tree according to the magnitude
# relationship.
# NOTICE: the 'count' argument is not necessary for this algorithm alone, but it's a must for our later sorting
# algorithm.
def remove_top(heap, count):
    # the result to be returned
    result = heap[0]
    # move bottom value to top as the new root
    heap[0] = heap[count-1]
    # restore heap structure
    index = 0
    while True:
        # find children indices
        child1 = 2 * index + 1
        child2 = 2 * index + 2
        # if child index is out of bound, then use current index for comparison
        if child1 >= count:
            child1 = index
        if child2 >= count:
            child2 = index
        # if relationship restored (i.e. value at correct position) then stop
        if heap[index] >= heap[child1] and heap[index] >= heap[child2]:
            break
        # determine which child is to be swapped with current value: the larger one
        if heap[child1] > heap[child2]:
            swap_child = child1
        else:
            swap_child = child2
        # swap the values
        temp = heap[swap_child]
        heap[swap_child] = heap[index]
        heap[index] = temp
        index = swap_child
    return result


# After we figure out how to form a heap (i.e. add all values from a list into a heap) and get top (largest) value from
# a heap, it's finally the time to combine them into a sorting function.
# The idea of sorting a list using heap is that, after transferring the list into a heap, the algorithm repeatedly
# removes the root so that the value next to the root keeps popping up, hence guarantees order. This is a O(Nlog(N))
# algorithm, and uses no extra space except those for indices.
def heap_sort(values):
    make_heap(values)
    # Everytime a value is removed from the top, it's positioned at the bottom node (the last in the heap).
    # Then, by using a descending index, we shorten the heap's length by 1. This ensures that the removed top value
    # stays at the end of list during the rest of iterations.
    # We do the same thing to the shortened heap, until the tree is empty.
    for i in range(len(values), 0, -1):
        temp = remove_top(values, i)
        values[i-1] = temp


# As we finished with the problems regarding heaps and heap sorting, we now move onto the next O(Nlog(N)) algorithm -
# the quicksort algorithm.

# The basis of quicksort is recursion. It splits a list into two parts based on a divider: the LHS values are smaller
# than it, while the RHS values are larger than it. Then for these divided fractions, the method calls itself to
# handle them separately.
# Given a good divider, the optimal time cost of this algorithm is O(Nlog(N)). The worst case scenario is O(N^2).

# Quicksort can be realized using stacks. The implementation is as followed. It needs an extra function for recursion.
def quicksort_stack(values):
    # Sort the whole array.
    do_stack_quick_sort(values, 0, len(values) - 1)


# The arguments start and end is an indicator for recursion, the distance between which is to be shortened at every
# recursion. Initially, they indicate the start and end of the list.
def do_stack_quick_sort(values, start, end):
    # if start = end (only one item in the list)
    if start >= end:
        return
    divider = values[start]
    # divide and collect items into 2 lists
    before = []
    after = []
    for i in range(start + 1, end + 1):
        if values[i] < divider:
            before.append(values[i])
        else:
            after.append(values[i])
    # move items back into the array
    index = start
    while len(before) > 0:
        values[index] = before.pop()
        index += 1
    # after all items before the divider added back to the array, add the divider.
    values[index] = divider
    # mark current index as the midpoint
    midpoint = index
    index += 1
    # Add the rest items
    while len(after) > 0:
        values[index] = after.pop()
        index += 1
    # recursion: call itself, with new start & end points.
    do_stack_quick_sort(values, start, midpoint - 1)
    do_stack_quick_sort(values, midpoint + 1, end)


# Although the stack quick sort performs well, it needs multiple spaces to store values along the processing. A way of
# saving space is to pre-designate a space for moving values. Hence we have the following code.
# The algorithm first checks if the list is of length 1 or less, which means the splits have come to the end. After
# judging this, the first value in the list is taken as the divider (the choice of dividers is rather arbitrary, but it
# needs to be placed at the top so that it can be read by the algorithm).
# Then, two variables - lo and hi record the smallest index of LHS, and the largest index of RHS, to ensure that the
# entries placed at either side can be tracked. They also tracks the empty space after every move.
# The algorithm then enters a loop for placing values, until both sides meet. The divider is then placed in between,
# and recurse to sort both sides in the same manner.
def do_quicksort(values, start, end):
    if start >= end:
        return
    # at the very beginning, record divider so the first entry is empty.
    divider = values[start]
    lo = start
    hi = end
    while True:
        # define a flag so the inner loop can terminate the outer loop
        meet = False
        # move hi to the first value that's smaller than the divider
        while values[hi] >= divider:
            hi -= 1
            # hi and lo meets but no values find, then the dividing is complete - terminate the outer loop.
            if hi <= lo:
                break
        # at this point, hi is moved to a value that's smaller than the divider. check again whether hi meets lo. if so,
        # place the divider in the middle before terminating the loop.
        if hi <= lo:
            values[lo] = divider
            break
        # move the smaller value to LHS.
        values[lo] = values[hi]

        # we do the same things again to the LHS.
        while values[lo] < divider:
            lo += 1
            if lo >= hi:
                break
        if lo >= hi:
            lo = hi
            values[hi] = divider
            break
        values[hi] = values[lo]
    do_quicksort(values, start, lo - 1)
    do_quicksort(values, lo + 1, end)


def quicksort(values):
    do_quicksort(values, 0, len(values) - 1)
# The efficiency of quicksort (in place - the above version) varies by the initial placement of values, while the stack
# quicksort maintains a O(Nlog(N)) time cost. Although, in extreme cases, the runtime of in-place quicksort can reach
# O(N^2), it's still usually faster than stack quicksort. To prevent this worst case scenario, randomize the divider
# is a good idea.
# In-place quicksort is also preferred for its another feature: it supports parallel processing. Theoretically, a
# computer with O(N) processors can sort a list with N entries in O(log(N)) of time.


test1 = [5, 4, 3, 2, 1]
test2 = []
for k in range(7):
    test2.append(random.randint(0, 50))
make_heap(test2)
print(test2)
quicksort(test2)
print(test2)
