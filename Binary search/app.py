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

def binary_search(list, element):
    middle = 0
    start = 0
    end = len(list)
    steps = 0
    
    while(start <= end):
        print("step", steps, ":", str(list[start:end+1]))
        
        steps = steps + 1
        middle = (start + end) // 2
        
        if element == list[middle]:
            return middle
        if element < list[middle]:
            end = middle - 1 #updates the new end value to the middle value - 1
            # in [1,2,3,4,5], the middle is 2.5 which is rounded to 3
            # If element is less then 3, the new end becomes 3 - 1 which is 2 and the process repeats using two
        else:
            start = middle + 1 #similarly, if element is greater that middle, te new start value is now middle + 1
            # in [1,2,3,4,5], the middle is 2.5 which is rounded to 3
            # If element is greater than 3, the new start becomes 3 + 1 which is 4 and the process repeats using 4
    return -1

my_list = [1,2,3,4,5,6,7,8,9,10,11,12]
target = 1


binary_search(my_list, target)