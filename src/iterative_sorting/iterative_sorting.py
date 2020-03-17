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
            # swapping without pop and insert method
            arr[i], arr[smallest_index] = arr[smallest_index], arr[i]
            # arr.insert(i, arr.pop(smallest_index)

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
            if arr[i] > arr[i+1]:
                # swapping without pop and insert method
                arr[i], arr[i+1] = arr[i+1], arr[i]
                # arr.insert(i, arr.pop(i+1))
                sc += 1

    return arr

# bubble_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7])
# 0,1,2,3,4,5,6,7,8,9


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):
    # getting max value in list, if list is empty returns empty list
    if len(arr) >= 1:
        maximum = max(arr)
    else:
        return []

    # creates a list of zeros based on the maximum value
    counter = [0] * (maximum + 1)

    # counts each value in the list
    for i in arr:
        if i < 0:
            return "Error, negative numbers not allowed in Count Sort"
        else:
            counter[i] += 1

    # setting the index for original list at beginning
    ndx = 0
    # going thru the length of the counter list to use as index position
    for i in range(len(counter)):
        # go thru each value in counter if value is not zero,
        while 0 < counter[i]:
            arr[ndx] = i
            ndx += 1
            counter[i] -= 1

    return arr

# count_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7, 7])
# 0,1,2,3,4,5,6,7,8,9

