# A major problem of recursions is the use of system memory. When the problem solving involves large amount of (deep)
# recursions, the use of system memory becomes huge and could cause stack overflow. For example, the calculation of
# Fibonacci sequence exceeds the capability of normal PC when the length surpasses 50.
# This part introduces some methods for solving this problem, including some ways of re-structuring or removing
# recursions.

# We first look at the deletion of tail recursions. If the function ends with the recursive code (calls itself), it's
# called a tail recursion. The following function is an example of tail recursion.
def example_factorial(n):
    if n == 0:
        return 1
    result = n * example_factorial(n-1)
    return result


# The above algorithm can be transformed into a non-recursive version via iteration, hence removing the tail recursion.
# In the iteration, the algorithm performs the task of the original algorithm. Before the iteration ends, the function
# should set its argument to values along the (previous) recursions. We also needs a variable to track its return value.
# NOTICE: such iteration should stop when the recursion's stopping condition appears.
def factorial(n):
    result = 1
    while n != 0:
        result *= n
        n -= 1
    return result

