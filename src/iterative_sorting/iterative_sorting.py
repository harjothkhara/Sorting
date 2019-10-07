# TO-DO: Complete the selection_sort() function below


def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)

        # TO-DO: swap

    return arr


# TO-DO:  implement the Bubble Sort function below

arr = [2, 1, 8, 7, 6, 5]

# i = 0 j = 0,1,2,3,4 ---> [1, 2, 7, 6, 5, ..., 8]
# i = 1 j = 0,1,2,3 ---> [1, 2, 6, 5... 7, 8]  # no need to compare 7 & 8 (8 already max)
# i = 2 j = 0,1,2 --> [1, 2, 5..., 6, 7, 8]  # no need to compare 6 to 7,8(sorted)
# i = 3 j = 0,1 --> [1, 2, ..., 5, 6, 7, 8]  # last items on the list already sorted
# i = 4 j = 0 ---> [1, ... 2, 5, 6, 7, 8]

# i through each iteration is controlling the ordered vs unordered border
# j is going through the unorderedlist (on the left) and comparing neighboring items amd swaping them

# i = 0
# j = 0


def bubble_sort(arr):
    # Loop through your array. Not including the last sorted item on the right at -1 - i
    for i in range(0, len(arr) - 1):
        for j in range(0, len(arr) - 1 - i):
            # Compare each element to its neighbor
            if arr[j] > arr[j+1]:
                # If elements in wrong position (relative to each other, swap them)
                arr[j], arr[j+1] = arr[j+1], arr[j]
# If no swaps performed, stop. Else, go back to the element at index 0 and repeat step 1.
    return arr


# print(bubble_sort(arr))
# Big O notation, tells us how the amount of operations our algorithm requires will grow as the size of our input grows. Bubble sort is O(n^2) time complexity.

# STRETCH: implement the Count Sort function below


def count_sort(arr, maximum=-1):

    return arr
