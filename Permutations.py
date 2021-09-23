# Recursion can also be used for calculating selection, combination and permutation. We first look into selection based
# on iterations.
# This algorithm simply iterates through every item and assemble them together. The very apparent drawback of this
# algorithm is that the length of selection must be pre-determined and implemented in the code structure.
def select_3_duplicates(items):
    result = []
    for i in range(len(items)):
        # to realize non-duplicate selection, we simply start every other iteration at the index next to the previous
        # cursor.
        # for j in range(i, len(items)):
        for j in range(i + 1, len(items)):
            # for k in range(j, len(items)):
            for k in range(j + 1, len(items)):
                result.append(items[i] + items[j] + items[k])
    return result


# To realize the selection algorithm without pre-determining the result length, we use recursion. Everytime the function
# is called, it adds an entry into the result. If the result doesn't contain enough numbers of entries, the function
# recursively calls itself to add more entries.
def select_k_of_n(index, selections, items, results):
    # check if the final entry has been added
    if index == len(selections):
        # add the current result into the result list
        result = []
        for i in range(len(selections)):
            result.append(items[selections[i]])
        results.append(result)
    else:
        # acquire a minimum value available for next combination
        start = 0  # the value is used for the first time
        if index > 0:
            start = selections[index - 1]
            # To realize selection without duplicates, simply set the start to selection[index-1]+1 so that the function
            # doesn't visit previous value.
            # start = selections[index-1] + 1
        # perform the next selection
        for i in range(start, len(items)):
            # add the ith value into the result
            selections[index] = i
            # recursively add the remaining combination
            select_k_of_n(index + 1, selections, items, results)


# Similarly, we can also realize permutation with duplicates using recursion. The difference is that rather than taking
# a starting value to begin iterations, the permutation iterates through all values, so that it takes values in any
# order and generate all permutations.
def permute_k_of_n(index, selections, items, results):
    # check if all permutations are completed
    if index == len(selections):
        result = []
        for i in range(len(selections)):
            result.append(items[selections[i]])
        results.append(result)
    else:
        for i in range(len(items)):
            selections[index] = i
            permute_k_of_n(index + 1, selections, items, results)


# For permutations, to avoid duplicates, we alter the algorithm so that it doesn't choose all values for every
# permutation, but instead exempts any used value.
def permute_non_dup(index, selections, items, results):
    if index == len(selections):
        result = []
        for i in range(len(selections)):
            result.append(items[selections[i]])
        results.append(result)
    else:
        for i in range(len(items)):
            # make sure the ith value is not used
            used = False
            for j in range(index):
                if selections[j] == i:
                    used = True
            if not used:
                selections[index] = i
                permute_k_of_n(index + 1, selections, items, results)


target = ['a', 'b', 'c', 'd', 'e']
print(select_3_duplicates(target))


