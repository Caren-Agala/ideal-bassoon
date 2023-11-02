# this program performs a binary search in python
# binary search works by taking a sorted list and dividing it in half and searching through it until the target data is found

# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# it takes the first index, divides it by 2 and uses the answer to split the answer into two
# if the target data is less than the middle number, it searches the left half
# if the target data is greater than the middle number, it searches the right half
# it keeps splitting the list in half until the target data is found


# STEPS IN THIS CODE
# define a function that takes a list and a target parameter
# multiple variables: middle, start, end and steps
# recursiom or while loop to repeatedly loop through the data
# increase steps each time a spllit is done
# condition to track the target position