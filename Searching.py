import random
import math


# This part will cover the algorithms for searching a value within an ordered (sorted) list, based on no other more
# complex data structures but only on arrays.


# The first to look at is the linear search (a.k.a. exhaustive search). This algorithm simply iterates through all
# values in the array to find the target. Different from binary or interpolation search, the linear search algorithm
# can be implemented on linked lists, a result of the fact that we can't jump freely from one index to another in linked
# lists.
# NOTICE: linear search can be applied on unsorted arrays, but with less efficiency: in a sorted list, the algorithm
# can stop once the current value is larger than the target, indicating that there's no such value in the list anyways.
# In worst case scenario, the algorithm needs to iterate through the whole list only to find no target value. Therefore,
# the largest runtime is O(N). It's worth noting that the expected runtime is also O(N).
def linear_search(values, target):
    for i in range(len(values) - 1):
        if values[i] == target:
            return i
        if values[i] > target:
            return -1
    return -1


# The binary search algorithm uses splitting strategy to rapidly locate the fraction where the target value lies. More
# specifically, it tracks the possible maximum and minimum index of target value, which is set to be the array's tail
# and head correspondingly.
# Then, the algorithm calculates the index in the middle of the min and max indices (mid). If the value at index mid is
# smaller than the target value, the algorithm resets the range to (mid, max), and repeats itself to the array's RHS.
# Binary search is a O(log(N)) algorithm.
def binary_search(values, target):
    min_index = 0
    max_index = len(values) - 1
    while min_index <= max_index:
        mid_index = math.floor((max_index + min_index) / 2)
        if target < values[mid_index]:
            max_index = mid_index - 1
        elif target > values[mid_index]:
            min_index = mid_index + 1
        else:
            return mid_index
    return -1


# An advanced version of binary search is interpolation search. Instead of halving the array for every iteration, it
# calculates (estimates) the midpoint by the target's value. for example, if the max value is 100, then the target of
# 70 is expected to be in the 70% quantile of the array.
# Although the proof is omitted, the algorithm can guarantee O(log(log(N))) runtime in optimal scenario, where the
# distribution of values is perfectly uniform. On contrary, if the distribution is extremely skewed, the algorithm will
# have O(N) runtime.
def interpolation_search(values, target):
    min_index = 0
    max_index = len(values) - 1
    while min_index <= max_index:
        mid_index = math.floor(min_index + (max_index - min_index) *
                               (target - values[min_index]) / (values[max_index] - values[min_index]))
        if values[mid_index] == target:
            return mid_index
        if target < values[mid_index]:
            max_index = mid_index - 1
        elif target > values[mid_index]:
            min_index = mid_index + 1
        else:
            return mid_index
    return -1


def do_quicksort(values, start, end):
    if start >= end:
        return
    divider = values[start]
    lo = start
    hi = end
    while True:
        while values[hi] >= divider:
            hi -= 1
            if hi <= lo:
                break
        if hi <= lo:
            values[lo] = divider
            break
        values[lo] = values[hi]
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


test = []
for k in range(7):
    test.append(random.randint(0, 50))
test.append(10)
quicksort(test)
print(test)
print(interpolation_search(test, 10))
