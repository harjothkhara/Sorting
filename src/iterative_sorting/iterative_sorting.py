# TO-DO: Complete the selection_sort() function below
# Selection Sort: During each iteration select the smallest item from the unsorted partition and move it to the the sorted partition.


#     b. Swap the element at current index with the smallest element found in above loop
list = [4, 8, 3, 5]


def selection_sort(list):
    # loop through n-1 elements
    # i --> 0-2, don't iterate thru final index as the left side would've been sorted by then.
     # Start with current index = 0
    # 2.For all indices EXCEPT the last index:
    for i in range(0, len(list) - 1):
        cur_index = i
        for j in range(i+1, len(list)):
            # Loop through elements on right-hand-side of current index and find the smallest element
            if list[j] < list[cur_index]:
                cur_index = j  # swap index
        if cur_index != i:
             # swap values
            list[i], list[cur_index] = list[cur_index], list[i]
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)

    return list


print(selection_sort(list))

# TO-DO:  implement the Bubble Sort function below

#list = [2, 1, 8, 7, 6, 5]

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
