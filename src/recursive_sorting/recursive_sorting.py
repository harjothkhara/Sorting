# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    # merging sorted lists back together -
    elements = len( arrA ) + len( arrB )
    # start merging single elements together
    # arrA[0] < arrB[0]
    merged_arr = [0] * elements
    # TO-DO
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
list = [4, 3, 7, 2, 88, 4, 5, 2, 1, 300, 100, 200, 1000]

def merge_sort( arr ):
    # TO-DO
    # basecase

  #While your data set contains more than one item, split it in half

  #divide left and right side of list

  #Once you have gotten down to a single element, you have also *sorted* that element
  #(a single element cannot be "out of order")

 # recursively call merge_sort() on LHS
 # recursively call merge_sort() on RHS

    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
