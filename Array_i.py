import random


def index_of(value, target):
    index = 0
    for i in target:
        if value == i:
            return index
        index += 1
    return -1


def find_min(target):
    m = target[0]
    for i in target:
        if i < m:
            m = i
    return m


def find_max(target):
    m = target[0]
    for i in target:
        if i > m:
            m = i
    return m


# This is a very rough function for locating median in a list: it cannot be applied on lists with
# repeated values, nor can it handle lists with odd length.
# A smart way would be first sorting the list, and return the median based on its index.
def find_mid(target):
    for i in target:
        larger = 0
        smaller = 0
        for j in target:
            if j < i:
                smaller += 1
            if j > i:
                larger += 1
        if smaller == larger:
            return i


# To find the mode, one way is to iterate the list and count every value separately: this algorithm
# takes O(N^2) processing time.
# Another way includes also sorting the list first, and find longest repeating values. The following
# code implements this mindset, and is estimated to take O(Nlog(N)).
# NOTICE: as sorting is not being discussed in this part, the function only takes a sorted list as
# argument.
def find_mode_sort(target):
    # Tracking longest repeating entry
    best_run_start = -1
    best_run_length = 0

    run_start = 0
    curr = target[0]
    for i in range(0, len(target) - 1):
        # if spotting a different (new) value
        if target[i] != curr:
            # record previous length
            run_length = i - run_start
            # judge longest
            if run_length > best_run_length:
                # updates
                best_run_start = run_start
                best_run_length = run_length
            curr = target[i]
            run_start = i
    run_length = len(target) - run_start
    if run_length > best_run_length:
        best_run_start = run_start
        best_run_length = run_length
    return target[best_run_start]


# To append an entry at the end of an array is relatively easy. However, it can be a bit complex
# when inserting a value in the middle of one. Before inserting the value into the designated
# position, every entry after that position has to move backwards to clear the space.
# NOTICE: in Python, this function is initially implemented as the insert() function of List class.
def insert(target, value, position):
    for i in range(len(target)-1, position, -1):
        target[i] = target[i-1]
    target[position] = value


# The above function has some limitations. First, it can only take lists consisting of sortable
# entries, i.e. numbers, characters.
# A solution to the problem is checking equality among entries and use a separate list for storing
# counts.


ll = []
ll1 = [1, 2, 3, 3, 4, 4, 5, 5, 5, 6, 7, 7, 8]
for g in range(0, 11):
    ll.append(random.randint(0, 11))
print(ll)
insert(ll, "inserted", 6)
print(ll)
