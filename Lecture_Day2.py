# Bubble Sort
import random
arr = list(range(4))
random.shuffle(arr)
# less efficient solution then in daily project

#arr = [0, 1, 2, 3, 4]
#has_swapped: False
#i = 3


def bubble_sort(arr):
    has_swapped = True
  # When no swaps have occurred, return
    while has_swapped:
        print(arr)  # printing for each iteration
        has_swapped = False
    # Walk through each element in the array
        for i in range(0, len(arr) - 1):
          # If the element is out of order from the neighbor..
            if arr[i] > arr[i+1]:
                # Swap
                arr[i], arr[i+1] = arr[i+1], arr[i]
                has_swapped = True
    return arr


# print(bubble_sort(arr))

# pros: easy to implement/understand
# cons: very, very inefficient
# time complexity: O(n^2)
# best case: O(1) - an already/almost sorted array. worst case -- O(n^2)

####################################
# Selection Sort - sorted half and unsorted half, instead of picking the first item in the unsorted half and inserting it into the correct place on the sorted half(insertion sort), we're going to select the smallest item from the unsorted half. you scan your unsorted array and when you get the smallest one you put it at the end of your sorted half. everything starts of unsorted.

smallest_value = 5
l = [1, 2, 3, 5, 6, 8]


def selection_sort(arr):
  # Divide the array into sorted and unsorted
  # loop through each element
    # -1 b/c we don't need to compare last item in the list since it will already be the largest item.
    for i in range(len(arr) - 1):
        current_index = i
        smallest_index = current_index
    # Find the smallest element in the unsorted
        for j in range(current_index, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
    # Put the smallest element at the end of the sorted
    # Swap the first element of unsorted with the smallest element
        arr[smallest_index], arr[current_index] = arr[current_index], arr[smallest_index]
    return arr


print(selection_sort(arr))
