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


# print(selection_sort(arr))

###############################
# Recursion and Recursive sorting
###############################

# what is recursion? a function that calls itself

# factoria(5) - -> 5 * 4 * 3 * 2 * 1 = 120  ### or 5 * factorial(4)
# factoria(4) - ->     4 * 3 * 2 * 1 = 24   ### or 4 * factorial(3)
# factoria(3) - ->         3 * 2 * 1 = 6    ### or 3 * factorial(2)
# factoria(2) - ->             2 * 1 = 2    ### or 2 * factorial(1)
# factoria(1) - ->                 1 = 1    ### or 1 * factorial(0)

# factoria(5) = 5 * factorial(4)

# iterative - loop
# def factorial(num):
    total = 1 # O(n) - linear: uses constant amount of space, memory. space efficient
    for n in range(2, num + 1):
        total *= n
    return total
# print(factorial(5)) #120

# Two key parts to any recursive function
#     1. need a base case: when your recursion stops
#     2. recursive call

# recursive - calls itself
def factorial(num): # everytime we do a recursive call we're creating a new number
    print(num)  # O(n) - linear
    if num <= 1:  # base case or infinite loop(stack overflow)
        return 1
    return num * factorial(num - 1)


#print(factorial(5))  # 120 or 5 * factorial(4)
# time complexity is O(n) b/c how many recursive calls do we have to make? as many as our number.

# Space Complexity - how much space does something take up given a num of inputs. in place sorts like iterative sorts don't use any space--->sorting is all within the list, or constant space. sometimes sorting algorithms will use extra space. iterative is more space efficient then recursive. however, recursion is more elegant then iterative (less line of code), especially if its a large list were sorting through. use recursion when n's are not big and not worried about space. anything you can solve recursively you can solve iteratively. inplace swaps - insertion, bubble. quicksort and merge sort take extra space.
#
# count sort - time complexity is great. space complexity is len(n)
[1,5,2,6,8,2,6,8]
[0,1,2,0,0,1,2,0,2]
[1,2,2,5,6,6,8,8]

#Quick Sort = pivot
#" divide and conquer"

# O(n * log n)
# n = number of pivots
#1. correct position in final, sorted array
#2. Items to the left are smaller
#3. Items to the right are larger
# when array is 1 or 0 then that item is sorted

[3,5,1,6,8,9,2,4]
pivot=4
#everything < pivot to the left, everything > pivot to the right
[3,1,2,4,5,6,8,9]
# sort the sub arrays
[3,1,2,      4,       5,6,8,9]
#we know 4 is in the right place
# we recursively call quicksort on the sub array
# now pivot =2 in sub array
# make sure <2 is smaller, everything >2 is bigger in sub array
[1,   2,   3,      4,       5,6,8,9]
# now we know 2 is in the right place
# now we have a sub array of size 1 -1 which is sorted - base case
# base case is when our array we're trying to sort is 1 or 0 then we know its sorted
[1,2, 3, 4,       5,6,8,9]
# now we quick sort right side
#pivot = 9
# need to make sure everythin to the left is smaller and to the right is larger.
[1,2, 3, 4,       5,6,8,9]
# 9 is already in the right place so we sort 5,6,8
[1,2, 3, 4,       5,6,8,      9]
# so is 6,8 in the right place since everything to the left of new pivot=8 is smaller, nothing to the right. And then we arrive at final item of 5 which is our base case. our entire array is sorted!
[1,2, 3, 4,5,6,8,9]

import random
items = list(range(6))
random.shuffle(items)

def quicksort(items):
    print(f"SORTING: {items}")
    # basecase
    if len(items) <= 1:
        return items
    # 1. Select the last element as the pivot.
    pivot = items[-1]
    left = []
    right = []
    for i in range(len(items) - 1):
        item = items[i]
        if item < pivot:
            # 2. Move all elements smaller than the pivot to the left.
            left.append(item)
        else:
            # 3. Move all elements greater than the pivot to the right.
            right.append(item)
    print(f"LEFT: {left}, PIVOT: {pivot}, RIGHT: {right}")
    # 4. While LHS and RHS are greater than 1, repeat steps 1-3 on each side.
    return quicksort(left) + [pivot] + quicksort(right)

print(quicksort(items))
