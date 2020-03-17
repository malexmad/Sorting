# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    ndx = 0
    for x in range(0, max(len(arrA), len(arrB))):

        if arrA[x] > arrB[x]:
            merged_arr[ndx] = arrB[x]
            ndx += 1
        else:
            merged_arr[ndx] = arrA[x]
            ndx += 1

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    l_arr = arr[:(len(arr)//2)]
    r_arr = arr[(len(arr)//2):]

    ndx=0
    for x in l_arr:
        l_arr[]


    print l_arr, r_arr
    return arr


merge_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7])
# [0,1,2,3,4,5,6,7,8,9]


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
