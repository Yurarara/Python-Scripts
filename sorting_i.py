import random


# Sorting algorithms are implemented in numerous libraries of various coding languages. However, the
# meaning of writing a sorting algorithm form the scratch is that we can sometimes surpass the performance
# of those pre-defined methods in some specific scenarios.
# We begin with the O(N^2) algorithms. Although in general they are slower than the O(Nlog(N)) counterparts,
# their simplicity guarantees higher performance for small scaled data.

# Insertion Sorting: the fundamental idea of insertion sorting is to acquire an entry from input list and
# insert it into a proper position in the output list.
# Speed-wise, although it's a O(N^2) algorithm, it's fast enough for lists with length under 10,000.
def insertion_sort(values):
    for i in range(0, len(values)):
        for j in range(i,0,-1):
            if values[j] < values[j-1]:
                values[j], values[j-1] = values[j-1], values[j]


# Selection Sorting: the fundamental idea of selection sorting is to locate the least entry in the input
# list, and append it to the end of the sorted list.
def selection_sort(values):
    for i in range(0, len(values)):
        for j in range(i, len(values)):
            # the numbers before index i has been sorted
            # if there's a smaller number appearing after the current number
            if values[j] < values[i]:
                # switch their positions, this insures i is always the least among its following numbers
                temp = values[i]
                values[i] = values[j]
                values[j] = temp


# Bubble Sorting: the fundamental concept of bubble sorting is that, if a list is unsorted, there has to
# be at least one pair of values that's not following the sorted order. The algorithm therefore iterate
# through the list repeatedly while swapping unordered entries, until there's no such pair.
# NOTICE: after every iteration, at least one of the entries reaches its final position.
def bubble_sort(values):
    not_sorted = True
    while not_sorted:
        not_sorted = False
        for i in range(0, len(values)-1):
            if values[i+1] < values[i]:
                # when spotted, switch unordered entries
                temp = values[i]
                values[i] = values[i+1]
                values[i+1] = temp
                not_sorted = True


val = []
while len(val) < 6:
    val.append(random.randint(0, 20))
print(val)
bubble_sort(val)
print(val)
