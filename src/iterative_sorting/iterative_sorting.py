# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for j in range(i+1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        # TO-DO: swap
        if smallest_index != i:
            temp = arr.pop(smallest_index)
            arr.insert(i,temp)

    return arr

# selection_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7])
# 0,1,2,3,4,5,6,7,8,9

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    # repeat at the 0 index if there was a swap
    # need a swap counter
    # compare element to its neighbor
    sc = 1
    while sc >= 1:
        sc = 0
        for i in range(0, len(arr)-1):
            j = i+1
            if arr[i] > arr[j]:
                temp = arr.pop(j)
                arr.insert(i, temp)
                sc += 1

    return arr

# bubble_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7])
# 0,1,2,3,4,5,6,7,8,9


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr