import random


# We now move onto some sorting algorithms with less than O(Nlog(N)) runtime, a floor impossible to surpass as long as
# the algorithm involves comparisons of any kind. On the contrary, this means if there are algorithms that sort values
# without comparing them, they might be able to achieve this breakthrough.

# The first we discuss is countingsort. It performs very well for integers in small ranges (e.g. 1 million integers
# ranging from 0 to 1000). Its basic concept is to count the appearance of each number, and copy the values back into
# the result list in accordance to the counts.
def counting_sort(values):
    # first, we need to locate the largest value of the list.
    max_value = 0
    for i in values:
        if i > max_value:
            max_value = i
    # create a list to store counts, whose length should be the max value of the target list.
    counts = [0 for i in range(max_value + 1)]
    # count the appearance of every number
    for i in values:
        counts[i] += 1
    # copy the values back into the target list
    print(counts)
    index = 0
    for i in range(max_value + 1):
        # for every number till the max, copy for count[i] times
        for j in range(0, counts[i]):
            values[index] = i
            index += 1


test1 = [5, 4, 3, 2, 1]
test2 = []
for k in range(11):
    test2.append(random.randint(0, 20))
print(test2)
counting_sort(test2)
print(test2)
