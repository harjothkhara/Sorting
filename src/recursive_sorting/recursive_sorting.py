# TO-DO: complete the helpe function below to merge 2 sorted arrays
elements = 2
arrA = 3
arrB = 7

def merge( arrA, arrB ):
    # merging sorted lists back together -
    elements = len( arrA ) + len( arrB )
    # start merging single elements together
    # arrA[0] < arrB[0]
    merged_arr = []
    # TO-DO
    for i in range(elements):
      # checking to see if lists are empty and adjusting position of merged lists
        if len(arrA) == 0:
          merged_arr.append(arrB[0])
          arrB = arrB[1:]
        elif len(arrB) == 0:
          merged_arr.append(arrA[0])
          arrA = arrA[1:]
        #check to make sure LHS < RHS
        elif arrA[0] < arrB[0]:
           merged_arr.append(arrA[0])
           arrA = arrA[1:]
        # if everything is already in the right position
        else:
            merged_arr.append(arrB[0])
            arrB = arrB[1:]
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
arr = [4, 3, 7, 2, 88, 4, 5, 2, 1, 300, 100, 200, 1000]
pivot_index = 6

def merge_sort( arr ):
    # TO-DO
    # basecase
    if len(arr) <= 1:
      return list
  #While your data set contains more than one item, split it in half
    else:
      pivot_index = len(arr)/2
      #divide left and right side of list
      left = arr[:pivot_index] # 4, 3, 7, 2, 88, 4
      right = arr[pivot_index:] # 5, 2, 1, 300, 100, 200, 1000
  #Once you have gotten down to a single element, you have also *sorted* that element
  #(a single element cannot be "out of order"). once we've sorted them down to single elements only then do we return them to the merge function to be merged.
 # recursively call merge_sort() on LHS
 # recursively call merge_sort() on RHS

    return merge(merge_sort(left), merge_sort(right))
    # recursively calling function until base case is met, then return.


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
